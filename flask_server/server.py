from flask import Flask, render_template
import json
import requests
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt


# Initialize Flask
app = Flask(__name__, template_folder="templates")


def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    # subreddit = response["subreddit"]
    return meme_large


def get_data():
    url = "https://data.gov.bh/api/explore/v2.1/catalog/datasets/03-population-by-nationality-and-sex/records?limit=20"
    response = json.loads(requests.request("GET", url).text)
    return response


@app.route("/")
def welcome():
    meme_pic = get_meme()
    return render_template("index.html", meme_pic=meme_pic)


@app.route("/data")
def data():
    return get_data()


# Run the app
# if __name__ == "__main__":
#     app.run(debug=True)
