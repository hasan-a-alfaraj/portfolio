from flask import Flask, render_template


# Initialize Flask
app = Flask(__name__, template_folder="templates")




@app.route("/")
def index():
    return render_template("index.html")


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
