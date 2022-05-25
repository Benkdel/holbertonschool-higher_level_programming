#!/usr/bin/node

$(document).ready(() => {
    
    $('DIV#add_item').click(() => {
        var item = $('<li>Item</li>');
        $("UL.my_list").append(item);
    })

    $('DIV#remove_item').click(() => {
        $('UL.my_list li:last-child').remove();
    });

    $('DIV#clear_list').click(() => {
        $('UL.my_list').empty();
    });
});
