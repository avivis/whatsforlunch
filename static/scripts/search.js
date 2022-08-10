function search(search_url="/search?", search_value=document.getElementById('search_value').value, zip_code=document.getElementById('zip_code')) {
    let xhr = $.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + zip_code + '&key=' + config['GOOGLE_API_KEY']);
    xhr.done(function(data) {
        var position = {
            'lat': data.results[0].geometry.location.lat,
            'long': data.results[0].geometry.location.lng,
        };
        getCall(position, search_url, search_value)
    })
}

function getCall(position, url, search_value) {
    var lat;
    var long;
    
    lat = position['lat'];
    long = position['long'];

    let data = {"lat": lat, "long": long, "search_value": search_value};
    let queryString = $.param(data);
    window.location.replace(url + queryString);
}
