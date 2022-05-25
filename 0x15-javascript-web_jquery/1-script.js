#!/usr/bin/node

function jqueryChangeColor() {
    $(document).ready(() => {
        $("header").css({
            color: '#FF0000'
        });
    });
}
