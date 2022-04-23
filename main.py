import json
from flask import Flask, render_template
import requests




# setup the app
app = Flask(__name__)
app.secret_key = "A_simple_phrase"


# plugins
@app.route("/")
def home():
    news_json = requests.get(f"https://newsapi.org/v2/everything?q=crops&from=2022-03-23&to=2022-04-22&sortBy=date&apiKey=3d3aca73f7d54306beb399b4d73e11a0")
    news_json_str = news_json.text
    news = json.loads(news_json_str)['articles']
    return render_template("index.html", newses = news, nos = range(10))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/weather")
def weather():
    # weather json
    lat = 26.14
    lon = 91.73
    API_key = '22538e054719782037738ce38f8fac32'
    wthr_json = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric")
    wthr_json_str = wthr_json.text
    wthr = json.loads(wthr_json_str)

    # present
    city = wthr['name']
    country = wthr['sys']['country']
    cloudiness = wthr['clouds']['all']
    temp_present = wthr['main']['temp']
    temp_min = wthr['main']['temp_min']
    temp_max = wthr['main']['temp_max']
    humidity = wthr['main']['humidity']
    print(wthr_json_str)

    return render_template('weather.html',cloudiness = cloudiness,country = country, city = city, temp_present = temp_present, temp_max = temp_max, temp_min = temp_min, humidity = humidity)


# running the app
app.run(debug=True)