#!/usr/bin/node

const axios = require('axios').default;
const process = require('process');

const URL = process.argv[2];

axios.get(URL, {
}).then((response) => {
  let count = 0;
  const results = response.data.results;
  for (let i = 0; i < response.data.count; i++) {
    const characters = results[i].characters;
    for (let j = 0; j < characters.length; j++) {
      if (characters[j].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
}).catch((err) => {
  console.log(err.message);
});
