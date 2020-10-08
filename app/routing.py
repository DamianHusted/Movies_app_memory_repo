from app import app
from flask import Flask, render_template, redirect, url_for, request

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('index.html')
