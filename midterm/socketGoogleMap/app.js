var google_geocoding = require('google-geocoding');
var bodyParser = require('body-parser');
var express = require("express");
var app = express();
var server = app.listen(2000);
var io = require("socket.io").listen(server);

app.use(express.static(__dirname + '/'));
console.log("Simple static server listening at http://localhost:" + 2000);

//socket.io stuff
io.sockets.on('connection', function (socket) {
  socket.on('toSearch', function (data) {
    console.log(data.q);
    var locToSearch = data.q;
    console.log('You sent the name "' + locToSearch + '".');
    google_geocoding.geocode(locToSearch, function(err, location) {
      console.log(locToSearch);
      if( err ) {
        console.log('Error: ' + err);
      }else if(!location){
        console.log('No result.');
      }else{
        console.log('Latitude: ' + location.lat + ' ; Longitude: ' + location.lng);
        socket.emit('latLon', { lat: location.lat, lon: location.lng });     
      }
    });
  });
});