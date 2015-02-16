$(document).ready(function(){
    var alertbox = $('#check');
    var sensorbox = $('#sensor');
    var imagebox = $('#image');
    // var toggleButon = $('#toggle').button();
    var deviceOptions = $('#device_id');
    var onoffDiv = jQuery('<div/>',{class:'onoffswitch', text:'Hello'}).html();
    var inputType = jQuery('<input>',{type:'checkbox',name:'onoffswitch',class:'onoffswitch-checkbox',id:'image'});

    //<input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox" id="image">

    setInterval(function(){
        if (sensorbox[0].checked){
            $.get("/sensors/oxygen?t="+now.toString(), function(data){
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


function deviceToggle(deviceIndex) {

    //var selectedDevice = $("#device_id option:selected").text()
    var selectedDevice = $(deviceIndex).attr('id');
    console.log(selectedDevice);
    $.ajax({
        url: "/devices/"+selectedDevice + "/toggle",
        type: 'PUT',
        success: function(response){
            //alert( "Success!" );
        }
    });
};

