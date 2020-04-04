# from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for,jsonify
from flask_jsglue import JSGlue
from cs50 import SQL
import requests

# configure application
app = Flask(__name__)
JSGlue(app)

db = SQL("sqlite:///suggestions.db")

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("webappmain.html")
    else:
        r=request.form["select"]
        if request.form["optionsRadios"]=="option1":
            return render_template("webapp1.html",r=r)
        elif request.form["optionsRadios"]=="option2":
            return render_template("webapp2.html",r=r)


@app.route("/coordinates", methods=["GET","POST"])
def coordinates():
    if not request.args.get("lat"):
        raise RuntimeError("Missing lat")
    lat=request.args.get("lat")
    lon=request.args.get("lon")
    headers = {'user-key': '485d23115749217b9322a8c4b523d716'}
    url = "https://developers.zomato.com/api/v2.1/geocode"
    params={"lat":lat, "lon":lon}
    r = requests.get(url, params=params, headers=headers)
    r=r.json()
    return jsonify(r)
