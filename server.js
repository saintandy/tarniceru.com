var express = require('express');
var app = express();
var path = require('path');

app.use(express.static(__dirname + '/public'))

var server = app.listen(80, function() {
  console.log('We have started our server on port 80');
});

app.get('/', function(req, res) {
  res.sendFile(path.join(__dirname + '/public/index.html'));
});
