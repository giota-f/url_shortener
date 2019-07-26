from restapi import app
from flask import render_template, request, redirect
import sqlalchemy
#from .models import Link

### Endpoints ###
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_link', methods=['POST'])
def add_link():
    original_url = request.form['original_url']
    engine = sqlalchemy.create_engine(
            'mysql+mysqlconnector://root:password@10.1.1.5:3306/sqlalchemy',
    echo=True)
    # Define and create the table
    connection = engine.connect()
    print(connection)
    #return render_template('link_added.html',
        #new_link=link.short_url, original_url=link.original_url)
    return 'ok'
