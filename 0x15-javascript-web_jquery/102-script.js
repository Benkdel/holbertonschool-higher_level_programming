#!/usr/bin/node

$(document).ready(() => {
    $('INPUT#btn_translate').click(() => {
        var lang = $('INPUT#language_code').val();
        console.log(lang);
        $('INPUT#language_code').empty();

        var url = `https://www.fourtonfish.com/hellosalut/?lang=${lang}`;
        $.getJSON(url, (data) => {
            $('DIV#hello').text(data['hello']);
        });
    });
});
