from flask import Flask, render_template
import json
import requests
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt


# Initialize Flask
app = Flask(__name__, template_folder="templates")




@app.route("/")
def index():
    return render_template("index.html")


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
