$(document).ready(function(){
    setInterval(function(){
        var checkbox = $('#check')[0];
        if (checkbox.checked){
            alert('hello');
        }
    }, 3000);
});
