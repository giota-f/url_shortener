from restapi import app
from flask import render_template, request, redirect
from restapi import mysql
from .models import Link

### Endpoints ###
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_link', methods=['POST'])
def add_link():
    original_url = request.form['original_url']
    link = Link(original_url=original_url)
    mysql.session.add(link)
    mysql.session.commit()

    return render_template('link_added.html',
        new_link=link.short_url, original_url=link.original_url)
