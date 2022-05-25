#!/usr/bin/node

$(document).ready(() => {
    $("DIV#red_header").click(() => {
        $(this).css({
            color: '#FF0000'
        });
    });
});
