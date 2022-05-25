#!/usr/bin/node

$(document).ready(() => {
    $("DIV#toggle_header").click(() => {
        var hasRed = $("header").hasClass("red");
        $("header").removeClass();
        if (hasRed) {
            $("header").addClass("green");
        } else {
            $("header").addClass("red");
        }
    });
});
