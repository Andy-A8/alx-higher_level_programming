#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const results = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      const chars = results[i].characters;
      for (let j = 0; j < chars.length; j++) {
        if (chars[j].includes('/18')) {
          count++;
          j = chars.length;
        }
      }
    }
    console.log(count);
  }
});
