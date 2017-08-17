function setUp() {

  // Get the modal
  var modal = $('#myModal');

  // Get the image and insert it inside the modal - use its "alt" text as a caption
  var pic = $('.poster');
  var modalImg = $('.modal-content');
  var captionText = $("#caption");

  $('.has_watched_box').on('change', registerWatch);
  $('.delete_box').on('change', function(){
    $(this).parent().fadeOut(1000);
  });
  $('.delete_box').on('change', deleteWatch);

  pic.on('click', function(){
    console.log($(this).attr('src'));
      modal.css({display: 'block'});
      modalImg.attr('src', $(this).attr('src'));
      console.log(modalImg);
      $('#title').text($(this).attr('name'));
      $('#overview').text($(this).attr('overview'));

  var span = $("#close")[0];

  // When the user clicks on <span> (x), close the modal
  $(span).on('click', function() {
    modal.css({display: 'block'});
  });
});
}

function registerWatch(){
     console.log($(this).val());
     // $.post("/history", {
     //      'val': $(this).val()
     // });
     $.ajax("/history", {
          data: {
               'type': 'add',
               'val': $(this).val()
          },
          method: 'POST'
     })
}

function deleteWatch() {
     console.log($(this).val());
     // $.delete("/history", {
     //      'val': $(this).val()
     // });

     $.ajax("/history", {
          data: {
               'type': 'remove',
               'val': $(this).val()
          },
          method: 'POST'
     })

     // $.ajax({
     //      val: $(this).val(),
     //      url: '/history',
     //      type: 'DELETE',
     //      success: function(data) {
     //      }
     // });
}

$(document).on('ready', setUp)
