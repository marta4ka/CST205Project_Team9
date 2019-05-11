# CST205_Project_Team9
Color Palette:
Extracts domain color for a palette, printing out an exact image of it at the bottom. 

extract_palette.py:
This file takes an image and analyzes the image to extract its color values. 
It will then put the colors from the image into seperate boxes and then will place them sequentially and
horizontally on a blank canvas. When the canvas is created we will have two examples: a palette with the colors in the image,
and the original image with the palette beneath it.

flask_webpage.py:
This file is our main file for our palette converter program. It contains all our flask modules since we will be using Flask
web application. This is where we will be asking the user to upload an image and then display the image with its palette.
The first route will accept the upload, send the upload to our extract_palette file to get the color values, and obtain the
hex values. The second route function will be used to display the results.

