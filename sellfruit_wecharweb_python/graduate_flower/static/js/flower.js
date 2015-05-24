


$(function(){
    $(".flower_sum").each(function(index){
        $(this).attr('id', index);
    });
    $(".flower_name").each(function(index){
        $(this).attr('id', "name-" +  index);
    });
    $(".price").each(function(index){
        $(this).attr('id', "price-" +  index);
    });

    $(".sub").each(function(index){
        $(this).attr('id', "sub-" +  index);
    });
    $(".add").each(function(index){
        $(this).attr('id', "add-" +  index);
    });

    add_sub();

    $(".flower_sum").change(function(){
        sum_change.call(this);
    });

    $("#phone").change(function(){
        check_phone()
    });

    $("#submit").click(function(){
        if(!check_phone()){
            return false;
        }

        var flowers = new Array();

        $(".flower").each(function(){
            var id_str = this.id;
            var id_arr = id_str.split("-");
            console.log(id_arr);
            var radio_name = "date-" + id_arr[1] + "-" + id_arr[2];
            var radio = $("input[name='"+radio_name+"']:checked").val();
            console.log(radio_name);
            var aflower = {"type": id_arr[1], "date":radio};
            console.log(aflower);
            flowers.push(aflower);
            console.log(flowers);
        });

        var phone = $("#phone").val();
        var remark = $("#remark").val();
        var information = {"flowers": flowers, "phone": phone, "remark": remark};
        console.log(information);
        ajaxjson(information);
    });

});

function sum_change() {
    var id = this.id;
    var name_id = "#name-" + id;
    var price_id = "#price-" + id;
    var name = $(name_id).html();
    var price = $(price_id).html();

    var flower_id = "";
    var radio_id = "";


    var fid = "." + id;
    $(fid).remove();

    var sum = 0;
    if ($(this).val() != "") {
        sum = parseInt($(this).val());
    }

    for (var i = 0; i < sum; ++i) {
        flower_id = "flower-" + id + "-" + i;
        radio_id = "date-" + id + "-" + i;
        var html_str = flower_html(id, flower_id, name, price, radio_id);
        $("#order_flower").append(html_str);
    }
}


function add_sub(){
    $(".sub").click(function(){
        var id_str = this.id;
        var id_arr = id_str.split("-");
        var sum_id = "#" + id_arr[1]
        var sum = parseInt($(sum_id).val());
        if(sum > 0){
            --sum;
        }
        else{
            sum = 0;
        }

        $(sum_id).val(sum);
        sum_change.call($(sum_id)[0]);
    });
    $(".add").click(function(){
        var id_str = this.id;
        var id_arr = id_str.split("-");
        var sum_id = "#" + id_arr[1]
        var sum = parseInt($(sum_id).val());
        sum++;

        $(sum_id).val(sum);
        sum_change.call($(sum_id)[0]);
    });
}

function check_phone(){
    var phone =  $("#phone").val();
    if(phone.length != 6 && phone.length != 11){
        alert("请正确填写电话号码");
        return false;
    }
    return true;
}

function flower_html(flower_class, flower_id, name, price, radio_id){
    var html_str = "   <div class=\"panel panel-info flower " + flower_class  + "\" id=\"" +  flower_id + "\"> "
        +"         <div class=\"panel-heading\"> "
        +"           <h3 class=\"panel-title\">" + name + "(" + price + "元)" + "</h3> "
        +"         </div> "
        +"         <div class=\"panel-body\"> "
        +"           <div class=\"form-group\" style=\"font-size:1.2em;\"> "
        +"               <div><label >请选择取花时间(8:00~10:00)</label></div>"
        +"               <label class=\"radio-inline\"> "
        +"                     <input type=\"radio\" name=\"" + radio_id + "\"   value=\"0\" checked=\"checked\"> 26号 "
        +"                  </label> "
        +"                   <label class=\"radio-inline\"> "
        +"                     <input type=\"radio\" name=\"" + radio_id + "\"  value=\"1\"> 29号 "
        +"                   </label> "
        +"                   <label class=\"radio-inline\"> "
        +"                     <input type=\"radio\" name=\"" + radio_id + "\"  value=\"2\"> 30号 "
        +"                   </label> "
        +"             </div> "
        +"         </div> "
        +"  </div>";

    return html_str;
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
        url: "http://127.0.0.1:8000/graduate/flower/action/", //getBaseURL()+"/RequestAjaxPerInfo/",
        data: {"information": JSON.stringify(information)},
        async: true,
        dataType: "json",
        type: "POST",
        success: function (result) {alert("kkkk");
            console.log(result);
            if(result.statu){
                alert("订花成功,请在您选定的时间到快递服务中心领取!");
            }
            else{
                alert("非常抱歉,您此次订花没成功,请重新打开网页试试!");
            }
        }


    });
}