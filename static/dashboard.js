$(document).ready(function(){
    var alertbox = $('#check').button();
    var sensorbox = $('#sensor').button();
    var toggleButon = $('#toggle').button();
    var deviceOptions = $('#device_id');

    $.getJSON("deviceList",function(data){
        $.each(data, function(ind) {
            console.log(data)
            deviceOptions.append($("<option></option>").attr("value",data[ind]).text(data[ind]));
        });
    })

    setInterval(function(){
        if (alertbox[0].checked){
            alert('hello');
        }
        if (sensorbox[0].checked){
            $.get("sensor/oxygen?t="+now.toString(), function(data){
                $("p").text(JSON.stringify(data.oxygen));
                $.plot($("#placeholder"),[data.oxygen],options);
            },"json");
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

function deviceToggle() {
    var selectedDevice = $("#device_id option:selected").text()
    $.ajax({
        url: selectedDevice + "/toggle",
        type: 'PUT',
        success: function(response){
            alert( "Success!" );
            }
        });
};



