import pot
import snot
import os
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True  # For debug

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/lookup/upcoming", methods=["POST"])
def lookup_upcoming_form():
    return redirect(url_for('upcoming', 
                            from_crs=request.form['from-crs'], 
                            to_crs=request.form['to-crs']))

@app.route("/upcoming/<string:from_crs>/<string:to_crs>")
def upcoming(from_crs, to_crs):
    if not pot.is_valid_crs(from_crs) and not pot.is_valid_crs(to_crs):
        return "Sorry, invalid CRS. Cannot check journey data for this!"

    api = snot.NationalRailAPI(os.environ["NR_API_KEY"])
    upcoming_trains = api.get_next_trains(from_crs, to_crs, 7)

    return render_template("upcoming.html", 
                           upcoming = upcoming_trains, 
                           reverse_route_url=url_for('upcoming', from_crs = to_crs, to_crs = from_crs))

if __name__ == "__main__":
    app.run()
