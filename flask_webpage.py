"""
File Name: flask_webpage.py
Team N9ne: Herendira Camarillo, Marta Gubanova, Jose Morado, Marco Rosales
Date: 5/10/2019
Description: This file is our main file for our palette converter program. It
             contains all our flask modules since we will be using Flask
             web application. This is where we will be asking the user to
             upload an image and then display the image with its palette.
             The first route will accept the upload, send the upload to our
             extract_palette file to get the color values, and obtain the
             hex values. The second route function will be used to display
             the results.
"""
from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import NumberRange
from werkzeug.utils import secure_filename
from wtforms import IntegerField
from webcolors import hex_to_rgb
from flask_wtf import FlaskForm
from extract_palette import extract_colors
import uuid
import os
#this is our form for flask. We use it to accept the users uploaded image.
#this form specifies that we will only accept files that are image files.
class PhotoForm(FlaskForm):
    photo = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    palette_height = IntegerField('Palette Height', validators=[NumberRange(1, 10)])
    palette_outline_width = IntegerField('Palette Outline Width', validators=[NumberRange(1, 40)])
#We create an instance of the flask class
app = Flask(__name__)
#we create a class that will has the specifications for an uploaded object
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'abadsecretkey'
    MAX_CONTENT_LENGTH = 4 * 1024 * 1024
#configure app so that only we can use our secret key and also access extensions
#it loads/enables the configuration from Config using from_object
app.config.from_object(Config)
#we create our decorator to bind our function to the flask url
#we have both GET and POST because we are asking the user to
#import i.e.POST an image
@app.route('/', methods=['GET', 'POST'])
#this function is where the user will upload the image. When the image is
#uploaded, it will be read the color values
def upload_image():
    #we display our home screen using url1
    url1 = url_for("static", filename ="images/home.jpg")
    #researched how to use PhotoForm() and found an example at
    #https://pythonhosted.org/Flask-WTF/form.html
    #this provides a form for photo data using the flask_wtf module
    form = PhotoForm()
    #if the user uploads an image i.e. checks if upload is an image
    if form.validate_on_submit():
        #takes the color values of the image and displays them
        print(hex_to_rgb(request.form.get('palette_outline_color')))
        #we store the image data in an object
        image_info = form.photo.data
        #we want to make sure we are getting correct data
        #we secure the filename before storing it directly on the filesystem.
        filename = secure_filename(image_info.filename)
        #we use os to help us get the path of the file. We split the path into
        #the root and extension (seperate file type from file name) and return 2-tuple
        _, extension = os.path.splitext(filename)
        #we update filename to give a unique id to each of the files uploaded.
        #we do this using the os import and generate a random unique hex value
        filename = uuid.uuid4().hex + extension
        #we print the uploaded files name
        print(filename)
        #here we take all the info we have gathered and create a pallete (new iimage)
        #that will be displayed below the submitted image. This will show the colors
        #in the submitted image as well as their hex values
        image_info, palette, hex_values = extract_colors(image_info, palette_length_div=form.palette_height.data, outline_width=form.palette_outline_width.data,
                       outline_color=hex_to_rgb(request.form.get('palette_outline_color')))
        #we then create an object that will contain the image from our absolute (root) static directory
        #This makes it easier for us to find the image file
        image_database = os.path.join(app.root_path, 'static/images',  filename)
        #palette from image chosen from database
        image_palette = os.path.join(app.root_path, 'static/images', "pal"+filename)
        #now we add our list_of_hex to the session dictionary that is connected to app
        session['hex_values'] = hex_values
        #we then save our image_info and its data from image database
        image_info.save(image_database)
        #and we save the palette data to the directory i.e. image_palette object
        palette.save(image_palette)
        #when all the info is validated and organized (as done above), we will redirect
        #and display the uploaded image
        return redirect(url_for('display_image', name=filename, height=image_info.height, width=image_info.width))
    #we then render our html template
    return render_template('upload_image.html', form=form, src='default', homepage = url1)

#this decorator will specify that we want to redirect to the image that was uploaded
@app.route('/display_palette/<name>/<height>/<width>')
#this function is for our second flask webpage that will display the palette
#with the image
def display_image(name, height, width):
    #link to the homepage for the user to upload another image
    url_back = url_for("upload_image")
    #we first get the image so we can display it
    fetch_image = url_for('static', filename='images/' + name)
    #then we get the palette for the image to display it as well
    fetch_image_palette = url_for('static', filename='images/' + "pal" + name)
    #complimented version
    #complimented_image = url_for()
    #we specify the dimensions for the returned image
    height, width = adjust_dimensions(int(height), int(width))
    #we render the html template with all the necessary objects that are needed
    return render_template('display_image.html', src=fetch_image, src2=fetch_image_palette, height=height, width=width, hex_values=session.get('hex_values'), back=url_back)
#we use this function to create a custom height and width
def adjust_dimensions(height, width):
    if height < 850 and width < 850:
        return height, width
    else:
        while height > 850 and width > 850:
            height = int(height/2)
            width = int(width/2)
        return height, width

#display error message if something goes wrong
@app.errorhandler(413)
def error413(e):
    return render_template('413.html'), 413
#here is where we call the application to run it
if __name__ == '__main__':
    app.run(debug=True)
