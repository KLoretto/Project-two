// Create a map object
var myMap = L.map("map", {
  center: [37.983810, 23.727539],
  zoom: 2
});

// Add a tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?" +
"access_token=pk.eyJ1Ijoic29sb21vbm1pbGxlciIsImEiOiJjamd4MDduZ2QxdjNtMnFtcWticW4yZDdrIn0.UzUscd_xQuIDVRDmh2CZjw"
).addTo(myMap);

// An array containing each city's name, location, and Actor
var cities = [{
  location: [51.509865, -0.118092],
  name: "New Cross, London",
  Actor: "Gary Oldman"
},
{
  location: [41.5532, -70.6086],
  name: "Falmouth",
  Actor: "Casey Affleck"
},
{
  location: [34.0928, -118.3287],
  name: "Hollywood",
  Actor: "Leonardo DiCaprio"
},
{
  location: [51.4975, -0.1357],
  name: "Westminster, London",
  Actor: "Eddie Redmayne"
},
{
  location: [29.2097, -99.7862],
  name: "Uvalde",
  Actor: "Matthew McConaughey"
},
{
  location: [51.5074, -0.1278],
  name: "London",
  Actor: "Daniel Day-Lewis"
},
{
  location: [48.8285, 2.2188],
  name: "Hauts-De-Seine",
  Actor: "Jean Dujardin"
},
{
  location: [51.0577, 1.3081],
  name: "Hampshire",
  Actor: "Colin Firth"
},
{
  location: [34.0522, -118.2437],
  name: "Los Angeles",
  Actor: "Jeff Bridges"
},
{
  location: [34.0195, -118.2437],
  name: "Santa Monica",
  Actor: "Sean Penn"
},
{
  location: [51.5074, -0.1278],
  name: "London",
  Actor: "Daniel Day-Lewis"
},
{
  location: [32.5007, -94.7405],
  name: "Longview",
  Actor: "Forest Whitaker"
},
{
  location: [43.0987, -77.4419],
  name: "Fairport",
  Actor: "Phillip Seymour Hoffman"
},
{
  location: [32.736, -96.2753],
  name: "Terrell",
  Actor: "Jamie Foxx"
},
{
  location: [34.0195, -118.4912],
  name: "Santa Monica",
  Actor: "Sean Penn"
},
{
  location: [42.139, -83.2418],
  name: "Woodhaven",
  Actor: "Adrien Brody"
},
{
  location: [40.9126, -73.8371],
  name: "Mount Vernon",
  Actor: "Denzel Washington"
},
{
  location: [-41.2865, 174.7762],
  name: "Wellington",
  Actor: "Russell Crowe"
},
{
  location: [40.7489, -74.261],
  name: "South Orange",
  Actor: "Kevin Spacey"
},
{
  location: [43.7711, 11.2486],
  name: "Tuscany",
  Actor: "Roberto Benigni"
},
{
  location: [40.2091, -74.0386],
  name: "Neptune",
  Actor: "Jack Nicholson"
},
{
  location: [-27.5598, 151.9507],
  name: "TooWoomba",
  Actor: "Geoffrey Rush"
},
{
  location: [33.7701, -118.1937],
  name: "Long Beach",
  Actor: "Nicolas Cage"
},
{
  location: [37.978, -122.0311],
  name: "Concord",
  Actor: "Tom Hanks"
},
{
  location: [40.8116, -73.9465],
  name: "Harlem",
  Actor: "Al Pacino"
}
                  
];

var myIcon = L.icon({
    iconUrl: 'oscar.png',
    iconSize: [38, 95],
    iconAnchor: [22, 94],
    popupAnchor: [-3, -76],
});

// Loop through the cities array and create one marker for each city, bind a popup containing its name and Actor add it to the map
for (var i = 0; i < cities.length; i++) {
  var city = cities[i];
  L.marker(
      city.location, {
      icon: myIcon})
    .bindPopup("<h1>" + city.name + "</h1> <hr> <h3>Actor " + city.Actor + "</h3>")
    .addTo(myMap);
}
