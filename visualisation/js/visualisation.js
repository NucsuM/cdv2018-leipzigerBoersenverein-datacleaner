var mymap = L.map('mapid').setView([51.3391827 ,12.3810549], 11);
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(mymap);

        var circle = L.circle([51.3391827, 12.3810549], {
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.5,
            radius: 3600
        }).addTo(mymap);

        circle.bindPopup("<b>Hello world!</b><br>I am a popup.");