from flask import render_template
from app import app

from db import *

@app.route('/')
@app.route('/index')
def index():

	conn = DBLite("films.db")
	films = []
	for i in conn.query("select * from films order by view_date desc"):
        	films.append(i)

	return render_template("index.html", films=films)
