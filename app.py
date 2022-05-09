from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    searchterm = request.args.get("searchterm")
    return render_template("search.html",searchterm=searchterm)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)