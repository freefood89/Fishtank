$(document).ready(function(){
    setInterval(function(){
        var alertbox = $('#check')[0];
        var sensorbox = $('#sensor')[0];
        if (alertbox.checked){
            alert('hello');
        }
        if (sensorbox.checked){
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
