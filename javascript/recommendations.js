function setUp() {

  // Get the modal
  var modal = $('#myModal');

  // Get the image and insert it inside the modal - use its "alt" text as a caption
  var pic = $('.poster');
  var modalImg = $('.modal-content');
  var captionText = $("#caption");
  pic.on('click', function(){
    console.log($(this).attr('src'));
      modal.css({display: 'block'});
      modalImg.attr('src', $(this).attr('src'));
      console.log(modalImg);
      // captionText.innerHTML = $(this).alt;
  });

  // Get the <span> element that closes the modal
  var span = $("#close")[0];

  // When the user clicks on <span> (x), close the modal
  $(span).on('click', function() {
    modal.css({display: 'block'});
  });

}

$(document).on('ready', setUp)
