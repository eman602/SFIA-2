from application import app
from flask import render_template, request
import requests


@app.route('/buildingfullname', methods=['GET'])
def name():
    firstname=requests.get('http://service_2:5001/buildingfullname')
    secondname=requests.get('http://service3:5002/buildingfullname')
    fullname = firstname.text+ " "+secondname.text

    return fullname