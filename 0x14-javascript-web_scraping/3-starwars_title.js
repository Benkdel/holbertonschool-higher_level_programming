#!/usr/bin/node

const axios = require('axios').default;
const process = require('process');

const movieID = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/';

axios.get(URL + movieID + '/', {
}).then((response) => {
  console.log(response.data.title);
}).catch((err) => {
  console.log(err.message);
});
