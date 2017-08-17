$(document).ready(function(){
	$('.movie_night').hide();
  $('.welcome').hide();
  $('.btn').hide();
})

$(window).load(function() {
     $(".movie_night").each(function(i) {
          $(this).delay(400*i).fadeIn(2000);
     });
     $('.welcome').each(function(){
          $(this).delay(1000).fadeIn(2000);
     });
     $('.btn').each(function(){
          $(this).delay(2000).fadeIn(1000).animate({left: '70%'}, 2500);
        });
});
