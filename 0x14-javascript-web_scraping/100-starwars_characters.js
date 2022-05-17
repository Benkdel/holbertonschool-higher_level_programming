#!/usr/bin/node

const axios = require('axios').default;
const process = require('process');

const movieID = process.argv[2];
const URL_1 = 'https://swapi-api.hbtn.io/api/films/';
const URL_2 = 'https://swapi-api.hbtn.io/api/people/';


function getMovie() {
  return axios.get(URL_1 + movieID + '/');
}

function getCharacters() {
  return axios.get(URL_2);
}

Promise.all([getMovie(), getCharacters()])
  .then(response => {
    const movie = response[0];
    const characters = response[1];

    const charUrls = movie.data.characters;
     
    console.log(charUrls);
    console.log(characters.data);
    /*
    const charNames = [];

    for (let i = 0; i < charUrls.length; i++) {

    }*/




  }).catch(err => {
    if (err) {
      console.log(err.message);
    }
  });
