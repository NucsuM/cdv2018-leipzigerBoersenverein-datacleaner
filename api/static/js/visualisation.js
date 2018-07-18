// get cities coordinates from api
function get_cities(){
    var request = new XMLHttpRequest();
    request.open("GET",'http://localhost:5000/api',false);
    request.send(null);
    return request.responseText;          
}

//call and center map to Leipzig
var mymap = L.map('mapid').setView([51.3391827 ,12.3810549], 8);
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);


// set points on map
var cities = JSON.parse(get_cities()).cities;
for (i in cities){
    var lat = cities[i]['lat'];
    var lan = cities[i]['lan'];
    var rad = cities[i]['radius'] * 10;
    var circle = L.circle([lat, lan], {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: rad
    }).addTo(mymap);
}

/*
// set a cycle to a map
var circle = L.circle([51.3391827, 12.3810549], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 3600
}).addTo(mymap);
*/
// a popup
//circle.bindPopup("<b>Hello world!</b><br>I am a popup.");

