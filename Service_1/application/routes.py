from application import app
from flask import render_template, request
import requests

@app.route('/', methods=['GET', 'POST'])
def home():
    result = requests.get('http://service_4:5003/fullname')
    fullname = result.text
    print(fullname)
    return render_template('home.html', fullname=fullname, title='Home page')
    

