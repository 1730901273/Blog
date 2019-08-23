//全局变量
let url = "/image_codes/1111-2222/";
$('#login-form').submit(function(){
            $.ajax({
            type:"POST",
            url:"/usercontrol/login",
            data:{"username":$("#login-username").val(),
                "password":$("#login-password").val()
            },
            beforeSend:function(xhr){
                xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
            success:function(data,textStatus){
                let errors = data["errors"];
                if(errors.length==0){
                    location.reload();
                }
                else{
                    alert(errors);
                    let html = "<div class=\"alert alert-danger\">"
                    for (let key in errors){
                        html += errors[key]+"<br/>";
                    }
                    html += "</div>";
                    $("#login-modal .modal-header").after(html);
                }
            },
            error:function(XMLHttpRequest, textStatus, errorThrown){
                alert(XMLHttpRequest.responseText);
            }

        });

        return false;
    });

    $("#login-button").click(function(){
        $("#login-modal .alert").remove();
    });


    $('#register-form').submit(function(){
        $.ajax({
            type: "POST",
            url : url,
            data:{
               "code":$("#register-captcha").val()
            },
            dataType: 'json',
            beforeSend:function(xhr){
                xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
            success:function (data) {
                let errors = data["errors"];
                if(errors.length===0){
                    console.log("2222222");
                    $.ajax({
                        type:"POST",
                        url:"/usercontrol/register",
                        data:{"username":$("#register-username").val(),"email":$("#register-email").val(),
                              "password1":$("#register-password-1").val(),"password2":$("#register-password-2").val(),},
                        dataType:'json',
                        beforeSend:function(xhr){
                            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                        },
                        success:function(data,textStatus){
                            let errors = data["errors"];
                            if(errors.length==0){
                                location.reload();
                            }
                            else{
                                //alert(errors);
                                let html = "<div class=\"alert alert-danger\">"
                                for (let key in errors){
                                    html += errors[key]+"<br/>";
                                }
                                html += "</div>";
                                $("#register-modal .modal-header").after(html);
                            }

                        },
                        error:function(XMLHttpRequest, textStatus, errorThrown){
                            alert(XMLHttpRequest.responseText);
                        }
                    });

                }
                else{
                    console.log("555551111");
                    //alert(errors);
                    let html = "<div class=\"alert alert-danger\">"
                    for (let key in errors){
                        html += errors[key]+"<br/>";
                    }
                    html += "</div>";
                    $("#register-modal .modal-header").after(html);
                }
            },
            error:function(XMLHttpRequest, textStatus, errorThrown){
                alert(XMLHttpRequest.responseText);
            }
        });

        return false;
    });

    $("#register-button").click(function(){
        console.log("5555555");
        $("#register-modal .alert").remove();
    });

    $("#logout").click(function(){
        $.ajax({
            type:"POST",
            url:"/usercontrol/logout",
            beforeSend:function(xhr){
                xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
            success:function(data,textStatus){
                location.replace("/");
            },
            error:function(XMLHttpRequest, textStatus, errorThrown){
                alert(XMLHttpRequest.responseText);
            }
        });
        return false;
    });
//获取焦点触发
window.onload = function() {
     let oat = document.getElementById("register-captcha");
     oat.onclick = function() {
         console.log("123333");
        $.ajax({
            type:"GET",
            url: url,
            beforeSend:function(xhr){
                xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            },
            success:function(callback){
                console.log("1355666");

                let obj = document.getElementById("detectImg");
                obj.src = url;
            },
            error:function(XMLHttpRequest, textStatus, errorThrown){
                alert(XMLHttpRequest.responseText);
            }
        });

     }
};

