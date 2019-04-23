"""
File Name: main_page.py
Name: Marco Rosales
Description: We created a flask application.
"""
#from flask import render_template, request, redirect, jsonify, make_response

#flask is our framework class, we use this to create instances
#of web applications, we get our HTML file using render_template
from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from datetime import datetime
#from flask_wtf import FlaskForm
#from wtfforms import StringField, SubmitField
#from wtfforms.validators import DataRequired
#from datetime import datetime
# create an instance of the Flask class

app = Flask(__name__)
bootstrap = Bootstrap(app)
# route() decorator binds a function to a URL
#creates a route to our hello html
@app.route('/main')
def main():
    #We print something to the IP address
    return "Testing website to see if its up"
#We must do http://127.0.0.1:5000/main to have the code run.

#This decorator will direct to the upload image widget
@app.route("/image-uploader", methods = ["GET", "POST"])
#function to upload an image
def upload_image():

    return render_template("upload_image.html")
