import requests

API_KEY = #REMOVED API KEY
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}


def get_business(sterm, lat, long, limit = 50, radius = 1000):
    parameters = {'term' : sterm,
                  'latitude' : lat,
                  'longtidue' : long,
                  'radius' : radius,
                  'limit' : limit}
    response = requests.get(url = ENDPOINT, params= parameters, headers= HEADERS)
    business_data = response.json()['businesses']

    if(radius>10000):
        return business_data
    elif len(business_data) < 1:
        return get_business(sterm, lat, long, limit=50, radius = radius + 1000)
    else:
        return business_data

def get_names(businesses):
    name_data = []
    for business in businesses:
        name_data.append([business['name']])
    return name_data
