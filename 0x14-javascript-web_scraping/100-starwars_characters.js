#!/usr/bin/node

const axios = require('axios').default;
const process = require('process');

const movieID = process.argv[2];
const URL_1 = 'https://swapi-api.hbtn.io/api/films/';
const URL_2 = 'https://swapi-api.hbtn.io/api/people/';

async function getNextPage (page) {
  try {
    const response = await axios.get(`${URL_2}?page=${page}`);
    if (response.status === 200) {
      return response.data;
    }
  } catch (err) {
    console.log(err.message);
  }
}

async function getMovie (movieID) {
  try {
    const response = await axios.get(`${URL_1}${movieID}/`);
    if (response.status === 200) {
      return response.data;
    }
  } catch (err) {
    console.log(err.message);
  }
}

async function printAllCharactersofMovie () {
  const maxPage = 15;
  let page = 1;
  let fullCharList = [];
  let charsInMovie = [];

  /* Get full list of Characters */
  while (page < maxPage) {
    const data = await getNextPage(page);
    page++;
    fullCharList = fullCharList.concat(data.results);
    if (data.next === null) {
      break;
    }
  }

  /* get list of characters (URLS) in movie by ID */
  const data = await getMovie(movieID);
  charsInMovie = charsInMovie.concat(data.characters);

  for (let i = 0; i < charsInMovie.length; i++) {
    for (let j = 0; j < fullCharList.length; j++) {
      if (charsInMovie[i] === fullCharList[j].url) {
        console.log(`${fullCharList[j].name}`);
      }
    }
  }
}

printAllCharactersofMovie();
