$($(document).ready(function() {
  $('.hide').hide();
  $('.show0').show(500);
  $('.show1').show(1000);
  $('.show2').show(2000);
  $('.remove-height').click(function() {
    $('#existing_mem_form').removeClass('h-90vh');
  });
}));
