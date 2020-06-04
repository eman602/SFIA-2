from application import app, db
from flask import render_template, request
import requests
from application.models import Names

@app.route('/', methods=['GET', 'POST'])
def home():
    result = requests.get('http://service_4:5003/fullname')
    fullname1 = result.text
    fullnamedb= Names(fullname=fullname1)

    db.session.add(fullnamedb)
    db.session.commit()

    namesData=Names.query.all()
    #print(fullname)
    return render_template('home.html', fullname=fullname1, posts=namesData, title='Home page')