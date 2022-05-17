#!/usr/bin/node

const axios = require('axios').default;
const process = require('process');

const URL = process.argv[2];

axios.get(URL, {
  params: {}
}).then((response) => {
  console.log('code: ' + response.status);
}).catch((err) => {
  console.log('code: ' + err.response.status);
}).then(() => { });
