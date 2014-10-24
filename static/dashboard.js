$(document).ready(function(){
    var alertbox = $('#check').button();
    var sensorbox = $('#sensor').button();
    
    setInterval(function(){
        if (alertbox[0].checked){
            alert('hello');
        }
        if (sensorbox[0].checked){
            $.get("sensor/oxygen?n=10", function(data){
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
