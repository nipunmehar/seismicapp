from flask import Flask
from flask_pymongo import PyMongo
import paho.mqtt.client as mqtt


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home_template():
    if request_method == ['GET']:
        return render_template('home.html')
    else:
        after_date = request.form['date']
        return make_response(show_data(after_date))


@app.route('/results')
def show_data(date):


app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)