"use strict";
var map;
console.log("Javascript");
function bakeriesMap() {
  console.log("Javascript");

  var locations = [
    ["Maison Bertaux", 51.5123, -0.1344],
    ["Bageriet", 51.52949, -0.12047],
  ];

  var mapOptions = {
    center: new google.maps.LatLng(51.509865, -0.118092),
    zoom: 15,
    mapTypeControl: false,
    panControl: false,
    streetViewControl: false,
    zoomControl: false,
    disableDoubleClickZoom: true,
  };

  console.log("hello from js");

  map = new google.maps.Map(document.getElementById("map"), mapOptions);

  var marker, i;

  for (i = 0; i < locations.length; i++) {
    var p = new google.maps.LatLng(locations[i][1], locations[i][2]);
    marker = new google.maps.Marker({
      position: p,
      map: map,
    });
  }
}

google.maps.event.addDomListener(window, "load", bakeriesMap);
