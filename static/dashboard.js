$(document).ready(function(){
    var alertbox = $('#check').button();
    var sensorbox = $('#sensor').button();
    
    setInterval(function(){
        if (alertbox[0].checked){
            alert('hello');
        }
        if (sensorbox[0].checked){
            $.get("sensor?a=true&b=true", function(data){
                var sensorData = ""
                $.each( data, function(k, v){
                    sensorData = sensorData + k + ": " + v + "\n";
                });
                $("p").text(sensorData);
            },"json");
        }
    }, 3000);
});
