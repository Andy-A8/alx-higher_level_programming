#!/usr/bin/node

const request = require('request');
const movieid = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieid;

request(url, function (error, reponse, body) {
  console.log(error || JSON.parse(body).title);
});
