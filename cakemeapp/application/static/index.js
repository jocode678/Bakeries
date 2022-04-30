"use strict";

let map;

function getCoordinates(address) {
  address = document.getElementById("postcode");
}

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 51.5074, lng: 0.1272 },
    zoom: 8,
  });
}

window.initMap = initMap;
