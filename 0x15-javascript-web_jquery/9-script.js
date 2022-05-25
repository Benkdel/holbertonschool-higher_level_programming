#!/usr/bin/node

$(document).ready(() => {
    url = 'https://fourtonfish.com/hellosalut/?lang=fr';
    
    $.getJSON(url, (data) => {
        $('DIV#hello').text(data['hello']);
    });
});
