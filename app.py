from flask import Flask, render_template
from datetime import datetime
import array
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", launches = launches)

def fetch_spacex_launches():
    url = "https://api.spacexdata.com/v5/launches"
    response = requests.get(url)
    if response.status_code == 200:      
        return response.json()
    else:
        return []
    
def categorise_launches(launches): # Only 3 status' of launch
    successful = list(filter(lambda x: x["success"] and not x["upcoming"], launches))
    failed = list(filter(lambda x: not x["success"] and not x["upcoming"], launches))
    upcoming = list(filter(lambda x: x["upcoming"], launches))
    
    return {
        "successful": successful,
        "failed": failed,
        "upcoming": upcoming
    }

@app.template_filter("date_only")
def date_only_filter(s):
    date_object = datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date_object.date()


launches = categorise_launches(fetch_spacex_launches())


if __name__ == "__main__":
    app.run(debug=True)