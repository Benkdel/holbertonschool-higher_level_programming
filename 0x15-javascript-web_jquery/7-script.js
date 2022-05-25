#!/usr/bin/node

$(document).ready(()=> {

    url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

    $.getJSON(url, (data) => {
        $("DIV#character").append(data.name);
      });
});
