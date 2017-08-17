function setUp() {

  // Get the modal
  var modal = $('#myModal');

  // Get the image and insert it inside the modal - use its "alt" text as a caption
  var pic = $('.poster');
  var modalImg = $('.modal-content');
  var captionText = $("#caption");

  $('.has_watched_box').on('change', registerWatch);

  pic.on('click', function(){
    console.log($(this).attr('src'));
      modal.css({display: 'block'});
      modalImg.attr('src', $(this).attr('src'));
      console.log(modalImg);
      $('#title').text($(this).attr('name'));
      $('#overview').text($(this).attr('overview'));
      // captionText.innerHTML = $(this).alt;




  // $('img.poster').on('mouseenter', function (e) {
  //   var checkbox = $(this).next();
  //   console.log('entering', e.target.tagName, 'checkbox is ', checkbox.tagName);
  //   checkbox.css({visibility: 'visible'});
  // });
  //
  // $('img.poster').on('mouseout', function (e) {
  //   var checkbox = $(this).next();
  //   console.log('leaving', e.target.tagName, 'checkbox is ', checkbox.tagName);
  //   checkbox.css({visibility: 'hidden'});
  // })
  //
  // Get the <span> element that closes the modal
  var span = $("#close")[0];

  // When the user clicks on <span> (x), close the modal
  $(span).on('click', function() {
    modal.css({display: 'block'});
  });
});
}

function registerWatch(){
     // $('#title').text($(this).attr('name'));
     console.log($(this).val());
     $.post("/history", {
          'val': $(this).val()
     });
     // console.log($(this).attr('value'));
}

$(document).on('ready', setUp)
