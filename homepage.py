"""
File Name: homepage.py
Creator: Marco Rosales
Description: This file is the first version of our website for our project.
             The first page displays our project name and team members as
             well as the class name. The second route is for the user to
             submit an image.
What needs work: *Need to create a link to upload image OR put it all on
                 the same page.
                 *Need to put the image upload text prompt somewhere in
                 the center.
                 *Need to create a GUI for the image uploader prompt
"""#flask is our framework class, we use this to create instances
#of web applications, we get our HTML file using render_template
import os
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, u'Image only!'), FileRequired(u'File was empty!')])
    submit = SubmitField(u'Upload')



#bootstrap = Bootstrap(app)

@app.route('/home')
def homepage():
    url1 = url_for("static", filename ="home.jpg")
    return render_template('homepage.html', homepage = url1)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
    else:
        file_url = None

    return render_template('index.html', form=form, file_url=file_url)


if __name__ == '__main__':
    app.run()
