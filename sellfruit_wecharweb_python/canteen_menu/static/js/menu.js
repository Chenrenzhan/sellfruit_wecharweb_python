/**
 * Created by chenrenzhan on 2015/5/9.
 */




window.onload = function(){
    menuFixed("nav");//固定菜单

    click();

    $(".condition").each(function(){
        $(this).click(function(){
            ajaxjson(this.id);
        });
    });
}

function click(){

    $(".nav_menu-item").each(function(e){
        $(this).click(function(e){
            $("#s_0").css('display', 'none');
            $("#s_1").css('display', 'none');
            $("#s_2").css('display', 'none');
            var id = this.id;
            var s_id = "#s_" + id;

            $(s_id).toggle();
            e.stopPropagation(); //阻止事件冒泡，否则事件会冒泡到下面的文档点击事件
        });
    });

    $(document).click(function() {
        $("#s_0").css('display', 'none');
        $("#s_1").css('display', 'none');
        $("#s_2").css('display', 'none');
    });

    $(".nav_submenu-item").click(function (e) {
        $("#s_0").css('display', 'none');
        $("#s_1").css('display', 'none');//alert(this.id);var id = "#" + this.id + " a";
        $("#s_2").css('display', 'none');alert($(this).find('a')[0].href);
        var id = $(this).find('a')[0].id;
        id = "#floor_" + id;alert(id);
        scroll(id);
        e.stopPropagation();
    });

}

//滚动至锚标记点
function scroll(id1){
    var obj = $(id1);

    var dh = obj.offset().top;
    //var sh = $(window).scrollTop();
alert(id1);
    //$(window).scroll(function(){obj.css('top', $(document).scrollTop());});
    //$(window).scroll(function(){$('#test').css('top', $(document).scrollTop() + $(window).height() - $('#test').height());});
    //if(dh > 200){
    //    obj.css('top', dh - 50) ;
    //    alert(dh);
    //}
    //else if(dh < 200){
    //    obj.css('top', dh + 50) ;;
    //}
    //setTimeout(scroll(id1), 500);
    //if(Math.abs(dh - 200) < 60){
    //    clearTimeout(scroll(id1));
    //}
//alert(dh);
    //$(window).scrollTop(dh);
    //$("html, body").stop().animate({scrollTop:dh}, 2000);
    //alert($("html, body").scrollTop);

    //var sTop = $(window).scrollTop();
    //if(sTop > 130){
    //    obj.slideDown();
    }
}

//ajax通讯，必须在HTML界面某个地方加入<form>{% csrf_token %}</from>

function ajaxjson(condition){

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

    var menus;
    $.ajax({
        url:"http://127.0.0.1:8000/canteenmenu/", //getBaseURL()+"/RequestAjaxPerInfo/",
        data:{"condition":condition},
        async:true,
        dataType:"json",
        type:"POST",
        success:function(result){
            menus = result;
            update(result);
            //fill_table(afx_result);
            //afx_ajaxed=true;//如果已经ajax过了就不要重复ajax了

        }
    });
    //return menus;
}

//更新网页信息
function update(menus){
    var html = "<ul class=\"channellist\">";
    for(var i = 0; i < menus["menus"].length; ++i){
        html += "<li>"
             +" <a >"
             +"      <div class=\"ChannelIcon\" style=\"margin-bottom: 10px; margin-top: 10px; \">"
             +"          <span class=\"name\" style=\"color: #ff9900; font-size: 1em;\">"
             + menus["menus"][i]["name"]
             +"          </span>"
             +"      </div>"
             +"      <div class=\"ChannelName\" style=\"margin-left: 0px; margin-right: 0px;\">"
             +"          <span style=\" font-weight:normal;font-size: 0.8em;\">"
             + menus["menus"][i]["price"] + "元/份"
             +"          </span>"
             +"      </div>"
             +"  </a>"
             +"</li>";
    }

    html += "</li>";
    document.getElementById("content").innerHTML = "";
    $("#content").innerHTML = "";
    document.getElementById("content").innerHTML = html;
    //$("#content").innerHTML = html;
}


 function menuFixed(id){
     var obj = document.getElementById(id);
     var _getHeight = obj.offsetTop;
     window.onscroll = function(){
         changePos(id,_getHeight);
     }
 }

function changePos(id,height){
    var obj = document.getElementById(id);
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    if(scrollTop < 200){
        obj.style.position = 'relative';
    }
    else{
        obj.style.position = 'fixed';
    }
}
