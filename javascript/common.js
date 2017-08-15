var images = ['#one', '#two','#three','#four','#five','#six','#seven']
imageIndex = 0
currentImage = $('#one')
fadeDuration = 3000

$(document).ready(function(){
	$('.photo').hide();
})

$(window).load(function() {
     $(".photo").each(function(i) {
          $(this).delay(400*i).fadeIn(1000);
     });
});

// $(document).ready(function() {
//
//     $('.photo').hide();
//     $('#one').each(function(i) {
//         if (this.complete) {
//             $('#one').fadeIn();
//         } else {
//             $(this).load(function() {
//                 $('#one').fadeIn(4000);
//             });
//         }
//     });
// });
//
// $(document).ready(function() {
//
//     $('.photo').hide();
//     $('#two').each(function() {
//         if (this.complete) {
// 					setTimeout(3000);
//           $('#two').fadeIn(4000);
//         }
// 				else {
//             $(this).load(function() {
// 							setTimeout(3000);
//             		$('#two').fadeIn(4000);
//             });
//         }
//     });
// });
