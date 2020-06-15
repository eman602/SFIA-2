from application import app
from flask import render_template, request
import requests


@app.route('/fullname', methods=['GET'])
def name():
    firstname=requests.get('http://service_2:5001/buildingfullname')
    secondname=requests.get('http://service_3:5002/buildingfullname2')
    fullname = firstname.text+ " "+secondname.text

    return fullname



