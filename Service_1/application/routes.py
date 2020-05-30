from application import app
from flask import render_template, request
import requests

@app.route('/', methods=['GET'])
def home():
    result = requests.get('http://35.223.230.68:5003/fullname')
    fullname = result.text
    print(fullname)
    return render_template('home.html', fullname=fullname, title='Home page')
    

