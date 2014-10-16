(function() {
    window.onload = function() { 
    // Creating a reference to the mapDiv
        var mapDiv = document.getElementById('map');
        
        // Creating a latLng for the center of the map
        var latlng = new google.maps.LatLng(57.414936, -6.726326999999969);
    
        // Creating an object literal containing the properties 
        // we want to pass to the map  
        var options = {
          center: latlng,
          zoom: 11,
          mapTypeId: google.maps.MapTypeId.SATELLITE
        };
        // Creating the map
        var map = new google.maps.Map(mapDiv, options);
        var fenway = new google.maps.LatLng(57.414936, -6.726326999999969);
                var mapOptions = {
                    center: fenway,
                    zoom: 14
                };
        var panoramaOptions = {
                position: fenway,
                pov: {
                    heading: 0.78,
                    pitch: -0.76
                },
                linksControl: false,                    
                panControl: false,
                zoomControl: false
            };
        
        var panorama = new google.maps.StreetViewPanorama(document.getElementById('pano'), panoramaOptions);
        map.setStreetView(panorama);    
        google.maps.event.addListener(
            panorama,
            'visible_changed',
            function() {
                //document.getElementById('lat').innerHTML = "Latitude: " + mapOptions.center.k;
                //document.getElementById('lng').innerHTML = "Longitude: " + marker.position.lng();
                console.log(panorama.getPosition().k);
                console.log(panorama.getPosition().B);
                var encounter = Math.round(Math.random()*10);
                console.log(encounter);
                if(encounter>8){
                    console.log("ALIEN!!");
                    renderAlien(panorama.getPosition().k, panorama.getPosition().B);
                    alienState = true;
                }//else{
                 //   alienState = false;
                //}

            }

        );
    }
})();