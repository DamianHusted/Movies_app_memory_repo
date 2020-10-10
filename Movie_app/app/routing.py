from flask import Flask, render_template, redirect, url_for, request
from Movie_app.app import app

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('index.html')
