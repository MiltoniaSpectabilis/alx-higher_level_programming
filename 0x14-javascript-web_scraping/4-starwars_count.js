#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (err, res, body) => {
	if (err) return console.error(err);

	const moveId = body.split('people/18/').length - 1;
	console.log(moveId);
});

