from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Scrape_Mars


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():

    destination_data = mongo.db.collection.find_one()

    return render_template("index.html", mars_data=destination_data)

@app.route("/scrape")
def scrape():
    
    mars_data = Scrape_Mars.scrape_info()

    mongo.db.collection.update({}, Scrape_Mars, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
