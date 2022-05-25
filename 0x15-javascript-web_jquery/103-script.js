#!/usr/bin/node

$(document).ready(() => {

    function sayHello() {
        var lang = $('INPUT#language_code').val();
        $('INPUT#language_code').empty();

        var url = `https://www.fourtonfish.com/hellosalut/?lang=${lang}`;
        $.getJSON(url, (data) => {
            $('DIV#hello').text(data['hello']);
        });
    }

    $('INPUT#btn_translate').click(() => {
        sayHello();
    });

    $('INPUT#language_code').focus(() => {
        $(this).keydown((e) => {
            if (e.which == 13) {
                sayHello();
            };
        });
    });
});

