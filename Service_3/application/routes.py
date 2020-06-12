from application import app
from flask import render_template, request
import random

@app.route('/buildingfullname2', methods=['GET'])
def secondname():
    list2=['benson', 'hesketh', 'ahmed', 'jennifer', 'oskar']
    response2=list2[random.randint(0, len(list2)-1)]

    return response2.upper()
    