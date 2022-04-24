
import json
from flask import Flask, render_template, request, flash
import requests
from flask_sqlalchemy import SQLAlchemy



# setup the app
app = Flask(__name__)
app.secret_key = "A_simple_phrase"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:58672@localhost/login'
# db = SQLAlchemy(app)



# class Login(db.Model):

#     # sno,name, email_id, phone_number, password
    
#     sno = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(100), unique=False, nullable=False)
#     password = db.Column(db.String(20), nullable=False)

# class Support(db.Model):

#     # sno,name, age, phone_number, gender, city/village, state, country, message
    
#     sno = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(100), unique=False, nullable=False)
#     age = db.Column(db.Integer(20), nullable=False)
#     phonenumber = db.Column(db.String(100), nullable=False)
#     city_village = db.Column(db.String(100), nullable=False)
#     state = db.Column(db.String(100), nullable=False)
#     country = db.Column(db.String(100), nullable=False)
#     message = db.Column(db.String(100), nullable=False)



# plugins
@app.route("/")
def home():
    news_json = requests.get(f"https://newsapi.org/v2/everything?q=crops&sortBy=date&apiKey=3d3aca73f7d54306beb399b4d73e11a0")
    news_json_str = news_json.text
    news = json.loads(news_json_str)['articles']
    return render_template("index.html", newses = news, nos = range(10))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blogs():
    return render_template('blogs.html', ros = range(6))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if(request.method=='POST'):
        name = request.form.get('name')
        password = request.form.get('password')
        entry = Login(name=name, password=password)
        db.session.add(entry)
        db.session.commit()
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
    wthr_main = wthr['weather'][0]['main']
    wind_speed = wthr['wind']['speed']
    print(wthr_json_str)

    # forcast
    cnt = 7
    # frcst_json = requests.get(f'api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt={cnt}&appid={API_key}')
    # frcst_json_str = frcst_json.text

    with open("forcast_sample.json","rt") as f:
        frcst_json_str = f.read()
    frcst = json.loads(frcst_json_str)
    return render_template('weather.html', nos = range(7) ,cloudiness = cloudiness,country = country, city = city, temp_present = temp_present, temp_max = temp_max, temp_min = temp_min, humidity = humidity, wthr_main = wthr_main, wind_speed = wind_speed, frcst = frcst)

@app.route("/financial")
def financials():
    return render_template("financial.html")

@app.route("/support",methods=['GET', 'POST'])
def support():
    if(request.method=='POST'):
        # name = request.form.get('name')
        # age = request.form.get('age')
        # phonenumber = request.form.get('phonenumber')
        # city_village = request.form.get('city_village')
        # state = request.form.get('state')
        # country = request.form.get('country')
        # message = request.form.get('message')
        # entry = Login(name=name, age=age, phonenumber=phonenumber, city_village = city_village,state= state,country=country,message=message )
        # db.session.add(entry)
        # db.session.commit()
        flash("your form is submitted successfully")

    return render_template("support.html")


# running the app
app.run(debug=True)