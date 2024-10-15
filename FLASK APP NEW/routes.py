from __main__ import app

from flask import Flask,render_template,flash,redirect,url_for,session,request
# we need request, session, flash and redirect for our logins
#from forms import NameForm,LoginForm

#importing database will allow us access the databases from the db_connector file
from db_connector import database
# pip install requests and hashlib
import requests
import hashlib

#define db as database
db = database()

@app.route('/')
def home():
    current_user = session.get('user')

    return render_template('home.html', name="Jack Webster", current_user=current_user)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("Contact.html")

@app.route('/game_details/<int:game_id>')
def game_details(game_id):
    game = db.queryDB("SELECT * FROM games WHERE game_id = ?",[game_id])
    return render_template('game_details.html', game=game)

@app.route('/delete/<int:game_id>')

def delete(game_id):
    # fetch game by ID
    db.updateDB("DELETE FROM game WHERE game_id= ?", [game_id])
    flash('Game Deleted !!!', 'success')
    return redirect (url_for('home'))
