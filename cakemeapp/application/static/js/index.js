"use strict";
var map;
console.log("Javascript");
function bakeriesMap() {
  console.log("Javascript");

  var locations = [
    ["Maison Bertaux", 51.5123, -0.1344],
    ["Bageriet", 51.52949, -0.12047],
    ["Cutter & Squidge", 51.51230, -0.13440],
    ["Aux Pains de Papy", 51.52949, -0.12047],
    ["Crumbs & Doilies", 51.51246, -0.13870],
    ["Miel Bakery", 51.52422, -0.13988],
    ["The Old Post Office Bakery", 51.46570, -0.12579],
    ["E5 Bakehouse", 51.54099, -0.05770],
    ["Fabrique Bakery Hoxton", 51.53231, -0.07536],
    ["Granier Bakery Cafe", 51.51334, -0.18790],
  ];

const infoWindow = new google.maps.InfoWindow();

  var mapOptions = {
    center: new google.maps.LatLng(51.509865, -0.118092),
    zoom: 12,
    mapTypeControl: false,
    panControl: false,
    streetViewControl: false,
    zoomControl: false,
    disableDoubleClickZoom: true,
  };

  console.log("hello from js");

  map = new google.maps.Map(document.getElementById("map"), mapOptions);

  var marker, i;
  var markers = [];

  for ( i = 0; i < locations.length; i++ ) {
    var p = new google.maps.LatLng(locations[i][1], locations[i][2]);
    marker = new google.maps.Marker({
      position: p,
      map: map,
      title: locations[i][0],
      optimized: false,
    });
     markers.push(marker);
     google.maps.event.addListener(marker, 'click', (function(marker, i) {
         return function() {

         infoWindow.close();
         infoWindow.setContent(marker.getTitle());
         infoWindow.open(marker.getMap(), marker);
         }
     })(marker, i));

  }


  };


google.maps.event.addDomListener(window, "load", bakeriesMap);
