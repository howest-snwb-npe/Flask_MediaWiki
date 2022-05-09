from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    searchterm = request.args.get("searchterm")
    #API code here
    #URL: https://test.wikipedia.org/w/api.php?format=json&action=query&list=search&srsearch=Japan

    url = f"https://test.wikipedia.org/w/api.php?format=json&action=query&list=search&srsearch={searchterm}"
    response = requests.get(url)

    article = response.json()["query"]["search"]
    for info in article:
      # print(json.dumps(info,indent=4))
      print(info["title"])
      print(info["snippet"])

    return render_template("search.html",searchterm=searchterm,article=article)

@app.route("/searchimage")
def searchimage():
    searchterm = request.args.get("searchterm")
    #URL:https://wikipedia.org/w/api.php?format=json&action=query&prop=pageimages&pithumbsize=100&titles=Albert%20Einstein 
    url = f"https://wikipedia.org/w/api.php?format=json&action=query&prop=pageimages&pithumbsize=100&titles={searchterm}"
    response = requests.get(url)
    image = response.json()["query"]["pages"]
    return render_template("searchimage.html",searchterm=searchterm,image=image)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)