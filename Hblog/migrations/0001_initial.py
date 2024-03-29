# Generated by Django 2.2.3 on 2019-07-26 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('en_title', models.CharField(max_length=100, verbose_name='英文标题')),
                ('img', models.CharField(default='/static/img/article/default.jpg', max_length=200)),
                ('tags', models.CharField(blank=True, help_text='用逗号分隔', max_length=200, null=True, verbose_name='标签')),
                ('summary', models.TextField(verbose_name='摘要')),
                ('content', models.TextField(verbose_name='正文')),
                ('view_times', models.IntegerField(default=0)),
                ('zan_times', models.IntegerField(default=0)),
                ('is_top', models.BooleanField(default=False, verbose_name='置顶')),
                ('rank', models.IntegerField(default=0, verbose_name='排序')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0, verbose_name='状态')),
                ('pub_time', models.DateTimeField(default=False, verbose_name='发布时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['rank', '-is_top', '-pub_time', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='导航条内容')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='指向地址')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '导航条',
                'verbose_name_plural': '导航条',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('summary', models.TextField(verbose_name='摘要')),
                ('news_from', models.IntegerField(choices=[(0, 'oschina'), (1, 'chiphell'), (2, 'freebuf'), (3, 'cnBeta')], default=0, verbose_name='来源')),
                ('url', models.CharField(max_length=200, verbose_name='源地址')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('pub_time', models.DateTimeField(default=False, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '资讯',
                'verbose_name_plural': '资讯',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='专栏内容')),
                ('summary', models.TextField(verbose_name='专栏摘要')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('article', models.ManyToManyField(to='Hblog.article', verbose_name='文章')),
            ],
            options={
                'verbose_name': '专栏',
                'verbose_name_plural': '专栏',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='名称')),
                ('rank', models.IntegerField(default=0, verbose_name='排序')),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hblog.Category', verbose_name='上级分类')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ['rank', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='摘要')),
                ('img', models.CharField(default='/static/img/carousel/default.jpg', max_length=200, verbose_name='轮播图片')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hblog.article', verbose_name='文章')),
            ],
            options={
                'verbose_name': '轮播',
                'verbose_name_plural': '轮播',
                'ordering': ['-create_time'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hblog.Category', verbose_name='分类'),
        ),
    ]
