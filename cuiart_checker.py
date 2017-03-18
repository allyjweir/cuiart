import pot
import snot
import os
from flask import Flask, render_template
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True  # For debug

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/upcoming/<string:from_crs>/<string:to_crs>")
def route_details(from_crs, to_crs):
    if not pot.is_valid_crs(from_crs) and not pot.is_valid_crs(to_crs):
        return "Sorry, invalid CRS. Cannot check journey data for this!"

    api = snot.NationalRailAPI(os.environ["NR_API_KEY"])
    upcoming_trains = api.get_next_trains(from_crs, to_crs, 7)

    return render_template("upcoming.html", upcoming = upcoming_trains)

if __name__ == "__main__":
            app.run()
