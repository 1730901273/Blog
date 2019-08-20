import time
import redis
# 连接池放到VisitCountMiddleware类外面
pool = redis.ConnectionPool(host='127.0.0.1', password='',port=6379,db=0)
# 注意类名必须是Ｍiddleware结尾。
class VisitCountMiddleware(object):
    def __init__(self, get_response):
        """统计访问量"""
        self.get_response = get_response
    def __call__(self, request):
        # 获取request的属性
        request_meta = request.META
        response =self.get_response(request)
        # 对要获取的参数进行判断，防止因没有参数而抛出异常
        # ip地址
        if request_meta.get("HTTP_X_FORWARDED_FOR"):
            ip = request_meta["HTTP_X_FORWARDED_FOR"]
        else:
            ip = request_meta["REMOTE_ADDR"]
        # 起始路径，可以统计在网站内部的访问记录，如：从A到B,起始路径就是A
        if request_meta.get('HTTP_REFERER'):
            HTTP_REFERER = request_meta['HTTP_REFERER']
        else:
            HTTP_REFERER = False
        # 目标路径，就是上面说到的B
        if request_meta.get('PATH_INFO'):
            PATH_INFO = request_meta['PATH_INFO']
        else:
            PATH_INFO = False
        # User-agent，这一项也可以用来过滤请求
        if request_meta.get('HTTP_USER_AGENT'):
            HTTP_USER_AGENT = request_meta['HTTP_USER_AGENT']
        else:
            HTTP_USER_AGENT = False
        # 请求方式
        if request_meta.get('REQUEST_METHOD'):
            REQUEST_METHOD = request_meta['REQUEST_METHOD']
        else:
            REQUEST_METHOD = False
        # 连接方式，
        if request_meta.get('HTTP_CONNECTION'):
            HTTP_CONNECTION = request_meta['HTTP_CONNECTION']
        else:
            HTTP_CONNECTION = False
        # 响应码
        response_code = response.status_code
        visit_time = time.strftime("%Y-%m-%d %H:%M:%S")
        # 组装数据，添加访问时间visit_time
        info_list = {
            'IP': ip,
            'Begin_path': HTTP_REFERER,
            'End_path': PATH_INFO,
            'User_agent': HTTP_USER_AGENT,
            'Request_method': REQUEST_METHOD,
            'Connection': HTTP_CONNECTION,
            'Response_code': response_code,
            'Visit_time': visit_time
        }

        # 调用存储数据库函数，存入数据库
        self.save_to_redis(info_list)
        return response

    def save_to_redis(self, info_list):
        """
                保存至Redis数据库
                :param result: type: dict
                :return:
                """

        # 数据库键名编号num，也是访问次数，从1开始
        num = 0
        # 连接数据库，try一下，捕获异常
        try:
            conn = redis.Redis(connection_pool=pool)
            # 在数据库中有访问次数，就是用数据库中的，如果没有（第一次），就使用上面的num=0，
            if conn.get('number'):
                # 因为redis数据库中键值对的值是以str类型储存的，下面需要进行加操作，因此需要转换成int
                print(info_list)
                num = int(conn.get('number'))
        except ConnectionError as e:
            print(e, '连接redis数据库失败')
        # 储存数据
        try:
            num += 1
            # 这里使用format动态创建键名，因为result是字典，所有，储存数据库时使用Hash数据类型，
            conn.hmset('visit_info{}'.format(num), info_list)
            # 如果数据储存如数据库，再把num存入数据库，键名为‘number’
            conn.set('number', num)
            print('成功存入redis数据库')
        except Exception as e:
            print(e, '储存redis数据库失败')
            pass

