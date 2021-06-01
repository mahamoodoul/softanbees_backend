$(document).ready(function() {
  $('#particles').particleground({
    dotColor: '#696969',
    lineColor: '#696969'
  });
  $('.intro').css({
    'margin-top': -($('.intro').height() / 2)
  });
});