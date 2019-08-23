window.onload = function() {
        let oat = document.getElementById("register-captcha1");
        const url = "/image_codes/1111-2222/";
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

                    let obj = document.getElementById("register-code");
                    obj.src = url;
                },
                error:function(XMLHttpRequest, textStatus, errorThrown){
                    alert(XMLHttpRequest.responseText);
                }
            });

         };
};
$('#vmaig-auth-register-form').submit(function(){
        const url = "/image_codes/1111-2222/";
        $.ajax({
            type: "POST",
            url : url,
            data:{
               "code":$("#register-captcha1").val()
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
                        data:{"username":$("#vmaig-auth-register-username").val(),"email":$("#vmaig-auth-register-email").val(),
                              "password1":$("#vmaig-auth-register-password1").val(),"password2":$("#vmaig-auth-register-password2").val(),},
                        dataType:'json',
                        beforeSend:function(xhr){
                            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                        },
                        success:function(data,textStatus){
                            let errors = data["errors"];
                            if(errors.length==0){
                                 location.replace("/");
                            }
                            else{
                                //alert(errors);
                                let html = "<div class=\"alert alert-danger\">"
                                for (let key in errors){
                                    html += errors[key]+"<br/>";
                                }
                                html += "</div>";
                                $("#vmaig-auth-register .panel-heading").after(html);
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
$("#vmaig-auth-register-button").click(function(){
        $("#vmaig-auth-register .alert").remove();
});