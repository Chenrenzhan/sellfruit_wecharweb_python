/**
 * Created by chenrenzhan on 2015/5/15.
 */


$(function(){
    $(".num").each(function(){
        var html = "";
        html += "<table class=\"table_num\" id=\"table_num\">"
        for(var i = 0; i < 5; ++i){
            for(var j = 0; j < 10; ++j){
                html += "<tr><td>" + j + "</tr></td>";
            }
        }
        this.innerHTML = html;
    });
});


$(function(){
    var width = $("#easing").width();
    var height = width * 0.625;
    console.log(width);
    console.log(height);

    var num_div = $("#num_div");
    var mask_div = $("#mask_div");
    var btn_div = $("#btn_div");

    var ml = width * 0.245;
    var mt = height * (-0.68);
    var div_visible_height = height * 0.30;
    num_div.css({
        "margin-left": ml,
        "margin-top": mt,
        "height" : div_visible_height,
        "overflow" : "hidden"
    });

    $(".table_num").each(function(){
        $(this).css({
            "font-size": width * 0.2
        });
    });


    var num_div_width = num_div.width();
    var num_div_height = num_div.height();
    ml = num_div.width();
    mt = num_div.height();

    var td_height = $(".table_num").height() / 50; //一个单元格高度
    $("#num1").css({
        "left": num_div_width * 0.062,
        "top": td_height * (-5),
    });
    $("#num2").css({
        "left": num_div_width * 0.40,
        "top": td_height * (-2),
    });
    $("#num3").css({
        "left": num_div_width * 0.72,
        "top": td_height * (0),
    });
//每次增加1.24
// -49.38, -50.62, -51.86, -53.10, -54.34, -55.58, -56.80, -58.04, 59.28, -60.52
    var ml = width * 0.245;
    var mt = height * (-0.25);
    mask_div.css({
        "margin-left": ml,
        "margin-top": mt
    });
});


function numRand() {
    var x = 999; //上限
    var y = 000; //下限
    var rand = parseInt(Math.random() * (x - y + 1) + y);
    return rand;
}
var isBegin = false;
$(function(){


    $('.btn_start').click(function(){

        var phoneNo = $("#phone").val();
        if(phoneNo.length != 6 && phoneNo.length != 11){
            alert("为了确保您中奖后领奖\r\n请正确填写手机号码");
            return false;
        }

        var information = getInformation();
        console.log(information);
        ajaxjson(information);


    });

});

$(function(){
    $("#phone").change(function(){
         var phoneNo = $(this).val();
         if(phoneNo.length != 6 && phoneNo.length != 11){
            alert("为了确保您中奖后领奖\r\n请正确填写手机号码");
        }
    });
});

function getInformation(){
    var phone = $("#phone").val();
    var wechatAccount = $("#wechat").val();
    var sex = $('input:radio[name="sex"]:checked').val();
    var single = $('input:radio[name="love"]:checked').val();

    return {"phone": phone, "wechat": wechatAccount, "sex": sex, "single": single};

}

function ajaxjson(information){
console.log(information);
    //django需要带上csrftoken
    var csrftoken = $.cookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    console.log("sasasaaaaaaaaaaaaaaaaaaad")
    $.ajax({
        url:"http://127.0.0.1:8000/wuerlingaction/", //getBaseURL()+"/RequestAjaxPerInfo/",
        data:{"information":JSON.stringify(information)},
        async:true,
        dataType:"json",
        type:"POST",
        success:function(result){console.log(result);

            var statu = result.statu;
            var lucknum = result.lucknum;
            var phone = information.phone;
            if(statu == 0){
                alert("号码：" + phone + "已参加了抽奖活动" + "\r\n每个号码只能摇一个号哦！");
                return false;
            }

            var POSITE = new Array();
            for(var i = 0; i < 10; ++i){
                POSITE[i] = -(40 + i);
            }
            var NUM_HEIGHT = $(".table_num").height() / 50;

            $(".num").css('top',0);

            var num_arr = (lucknum+'').split('');
            console.log(num_arr);
            $(".num").each(function(index){
                var _num = $(this);
                setTimeout(function(){
                    _num.animate({
                        top:  (NUM_HEIGHT * POSITE[num_arr[index]])
                    },{
                        duration: 6000 + index*1000,
                        easing: "easeInOutElastic"
                    });
                }, index * 300);

            });
            setTimeout(function(){
                    alert("您已成功参加活动" + "\r\n你抽到的幸运码是：" + lucknum
                    + "\r\n为方便您领奖，请记住您的幸运码");
                }, 10000);

        }
    });
}