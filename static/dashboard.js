$(document).ready(function(){
    var alertbox = $('#check');
    var sensorbox = $('#sensor');
    var imagebox = $('#image');
    var toggleButon = $('#toggle').button();
    var deviceOptions = $('#device_id');
    var onoffDiv = jQuery('<div/>',{class:'onoffswitch', text:'Hello'}).html();
    var inputType = jQuery('<input>',{type:'checkbox',name:'onoffswitch',class:'onoffswitch-checkbox',id:'image'});

    //<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox" id="image">

    $.getJSON("devices",function(data){
        $.each(data, function(ind) {
            console.log(data)
            deviceOptions.append($("<option></option>").attr("value",data[ind]).text(data[ind]));
            $("aside").append(data[ind] + '<div class="onoffswitch"> <input type="checkbox" onchange=deviceToggle(' + this + ') name="onoffswitch" class="onoffswitch-checkbox" id= "' + data[ind] + '"><label class="onoffswitch-label" for="' + data[ind]+ '"><span class="onoffswitch-inner"></span> <span class="onoffswitch-switch"></span> </div>');

        });
    });

    setInterval(function(){
        if (alertbox[0].checked){
            alert('hello');
        }
        if (sensorbox[0].checked){
            $.get("sensors/oxygen?t="+now.toString(), function(data){
                //$("p").text(JSON.stringify(data.oxygen));
                $.plot($("#placeholder"),[data.oxygen],options);
            },"json");
        }
        if (imagebox[0].checked){
            $.get('/recentImage', function(data){
                $('#RecentImage').attr("src",'/recentImage');
            }
            );
        }
    }, 3000);
});

var now = (new Date()).getTime();
var data = [[[now,1],[now+100000,2],[now+200000,3],[now+300000,2]]];
var options = {
    xaxis: {
        mode: "time",
        timeformat: "%m/%d %H:%M"
    },
    series: {
        lines: {show: true}
    }
};
$.plot($("#placeholder"),data,options);

function deviceToggle(deviceIndex) {
    //var selectedDevice = $("#device_id option:selected").text()
    var selectedDevice = $(deviceIndex).attr('id');
    $.ajax({
        url: "devices/"+selectedDevice + "/toggle",
        type: 'PUT',
        success: function(response){
            //alert( "Success!" );
        }
    });
};

