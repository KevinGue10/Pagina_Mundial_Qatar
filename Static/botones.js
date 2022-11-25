$(document).ready(function() {
    $(".btn-left").on("click", function() {
       $(".input-box").val(parseInt($(".input-box").val())-1);
    }); 
    $(".btn-right").on("click", function() {
       $(".input-box").val(parseInt($(".input-box").val())+1);
    }); 
 }); 