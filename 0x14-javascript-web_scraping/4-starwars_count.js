#!/usr/bin/node

const axios = require('axios').default;
const process = require('process');

const URL = process.argv[2];

axios.get(URL, {
}).then((response) => {
  let count = 0;
  const results = response.data.results;
  results.forEach(res => {
    res.characters.forEach(char => {
      if (char.includes('18')) count++;
    });
  });

  console.log(count);
}).catch((err) => {
  console.log(err.message);
});
