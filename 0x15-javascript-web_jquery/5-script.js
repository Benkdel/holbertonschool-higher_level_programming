#!/usr/bin/node

$(document).ready(() => {
    $("DIV#add_item").click(() => {
        var item = $("<li></li>").text("Item");
        $("UL.my_list").append(item);
    })
});
