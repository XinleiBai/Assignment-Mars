import sys
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

sys.setrecursionlimit(2000)
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"

client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_facts


@app.route('/scrape')
def scrape():
 
    mars = scrape_mars.scrape()
    print("\n\n\n")
    
    db.mars_facts.insert_one(mars)
    return "Some scrapped data"

@app.route("/")
def home():
    mars = list(db.mars_facts.find())
    print(mars)
    return render_template("index.html", mars = mars)


if __name__ == "__main__":
    app.run(debug=True)
