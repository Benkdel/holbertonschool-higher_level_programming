#!/usr/bin/node

$(document).ready(() => {

    
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    
    $.getJSON(url, (data) => {
        const films = [];
        
        data.results.forEach(r => {
            films.push(`<li>${r["title"]}</li>`);
        });

        $("UL#list_movies").append(films.join(""));
    });
});