#!/usr/bin/node

$(document).ready(() => {
    $("DIV#update_header").click(() => {
        $("header").html("New Header!!!");
    })
});
