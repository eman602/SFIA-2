from application import app
from flask import render_template, request
import random

@app.route('/buildingfullname', methods=['GET'])
def firstname():
    list=['Mark', 'James', 'Daniel','William', 'Emmanuel','Ellen']
    response1=list[random.randint(0, len(list)-1)]

    return response1
    