from flask import Flask, render_template



# setup the app
app = Flask(__name__)
app.secret_key = "A_simple_phrase"


# plugins
@app.route("/")
def home():
    return render_template("index.html")



# running the app
app.run(debug=True)