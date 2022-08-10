from flask import Flask, render_template, request
from yelpapi import get_business, get_business, get_names, get_names

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('search.html', results=search)

@app.route("/search")
def search():
    search_args = request.args 
    location = {
        'lat': search_args['lat'],
        'long': search_args['long']
    }
 
    businesses = get_business(search_args['search_value'], search_args['lat'], search_args['long'])
    bus_names = get_names(businesses)
    return search_results(businesses, location, bus_names, search_value=search_args['search_value'])

@app.route("/results")
def search_results(businesses, location,  bus_names=[], search_value=""):
    return render_template("results.html", search_value=search_value, businesses=businesses, location=location,
                           biz_locations=bus_names, google_api_key='AIzaSyBaFmWC5h6ehbNeZPbbhMm2G9S2hF2QgRU')


if __name__ == '__main__':
    app.run(debug = True)
