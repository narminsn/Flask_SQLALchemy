
var search_url="http://0.0.0.0:5001/?q=forest"
console.log("asdfg")
$(document).ready(function(e){
    $.ajax({
        url: search_url,
        method: "GET",
        success: function(data){
            console.log(data)
            $(".result").html(data.code)
        }
    })

});