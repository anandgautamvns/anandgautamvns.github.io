var action="click";
var speed="500";

$(document).ready(function(){
  $('.container.q').on(action ,function(){
    $(this).next()
      .slideToggle(speed)

    var img = $(this).children('img');
    $('img').not(img).removeClass('rotate');
    img.toggleClass('rotate');
  });
});
