var userName = document.getElementById("userName");
var password = document.getElementById("userPwd");
var inputCode = document.getElementById("inputCode");
var info = document.getElementById("info");

var flag=0;

var pa=/^[a-zA-Z0-9]{6,10}$/;

userName.onblur = function(){
        if(pa.test(userName.value)){
            info.innerHTML="用户名输入正确";
        }
        else{
            info.innerHTML="用户名输入错误";
        }
    }

password.onblur = function(){
        if(pa.test(password.value)){
            info.innerHTML="密码输入正确";
        }
        else{
            info.innerHTML="密码输入错误";
        }
}

inputCode.onblur = function(){
    
    //获取显示区生成的验证码
    var checkCode = document.getElementById("checkCode").innerHTML;
    //获取输入的验证码
    var inputCode = document.getElementById("inputCode").value;
    if (inputCode.length <= 0){
        info.innerHTML="请输入验证码！";
    }
    else if (inputCode.toUpperCase() != checkCode.toUpperCase()){
        info.innerHTML="验证码输入错误";
        createCode(4);}
    else
    {
        info.innerHTML="验证码正确！";
        flag=1;
    }       
}

    //回车键
    document.onkeydown = function (e) {
        if ((e.keyCode || e.which) == 13) {
            var btlogin = document.getElementById("btnclick");
            login();
        }
    };
    function login(){
        if(pa.test(userName.value)&&pa.test(password.value)&&flag==1){
            window.location.href = "index.html";
        }
    };