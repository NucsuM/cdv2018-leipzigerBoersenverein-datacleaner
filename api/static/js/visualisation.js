function get_cities(){
    var Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open("GET",'http://localhost:5000/api',false);
    Httpreq.send(null);
    return Httpreq.responseText;          
}

var json_obj = JSON.parse(get_cities());
for (i in json_obj.cities){
    console.log(json_obj.cities[i].lan)
}



//var test = get_cities()

document.getElementById('json').innerHTML=json_obj.cities[i]

/*
var mymap = L.map('mapid').setView([51.3391827 ,12.3810549], 11);
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);




for (i in cities) {
    var lat = cities[i]['lat'];
    var lan = cities[i]['lan'];
    var rad = cities[i]['radius'];
    var circle = L.circle([lat, lan], {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: rad
    }).addTo(mymap);
}





var circle = L.circle([51.3391827, 12.3810549], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 3600
}).addTo(mymap);

circle.bindPopup("<b>Hello world!</b><br>I am a popup.");
*/



