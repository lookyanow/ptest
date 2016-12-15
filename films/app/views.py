from flask import render_template
from app import app

from db import *
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():

	conn = DBLite("films.db")
	films = []
	for i in conn.query("select * from films order by view_date desc"):
		films.append(i)
		
	for film in films:
		film['view_date'] = str(datetime.fromtimestamp(film['view_date']).strftime('%d-%m-%Y'))

	return render_template("index.html", films=films)
