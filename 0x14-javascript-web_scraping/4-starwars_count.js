#!/usr/bin/node

const axios = require('axios').default;
const process = require('process');

const URL = process.argv[2];
const charID = 18;

axios.get(URL, {
}).then((response) => {
  let matches = 0;
  const nMovies = response.data.count;
  const results = response.data.results;
  for (let i = 0; i < nMovies; i++) {
    const characters = results[i].characters;
    for (let j = 0; j < characters.length; j++) {
      if (characters[j].includes(`${charID}`)) {
        matches += 1;
      }
    }
  }
  console.log(matches);
}).catch((err) => {
  console.log(err.message);
});
