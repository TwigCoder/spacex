import requests
from flask import Flask, render_template
import scraper

app = Flask(__name__)


@app.route("/")
def home():
    spacex_data = scraper.scrape_latest_launch()

    spacex_data["crew"] = []

    return render_template("index.html", launch_data=spacex_data)


if __name__ == "__main__":
    app.run(debug=True)
