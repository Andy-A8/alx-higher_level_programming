$('document').ready(function () {
  $('INPUT#btn_translate').click(fetchtranslate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (event) {
      if (event.keyCode === 13) {
        fetchtranslate();
      }
    });
  });
});

function fetchtranslate () {
  const url =' https://fourtonfish.com/hellosalut/hello/?'
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      $('DIV#hello').html(data.hello);
  });
}
