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

    url = "https://test.wikipedia.org/w/api.php?format=json&action=query&list=search&srsearch=Japan"
    response = requests.get(url)

    article = json.dumps(response.json(), indent=4)
    print(article)
    
    return render_template("search.html",searchterm=searchterm,article=article)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)