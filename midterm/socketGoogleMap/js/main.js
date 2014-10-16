//socket io
var socket;
var latitude;
var longitude;
$(document).ready(function(){
	socket = io.connect('http://localhost:2000');
	socket.on('latLon', function (data) {
		console.log(data);
		latitude = data.lat;
		longitude = data.lon;
		init(latitude,longitude);
	});
});
//When Search button is clicked emit data to socket
function toSearch(){
	var query = document.getElementById('text').value;
	socket.emit('toSearch', { q: query });
}