# CST205_Project_Team9
PaletteFinder

Website with a program that extracts dominant colors from an uploaded image to create two palettes: original colors and complementary colors, displying an image of them at the bottom of the page. 

extract_palette.py:
This file takes an image and analyzes the image to extract its color values. 
It will then put the colors from the image into separate boxes and then will place them sequentially and
horizontally on a blank canvas. When the canvas is created we will have two examples: 
a palette with the dominant colors from the image,
and the original image with the palette beneath it.

flask_webpage.py:
This file is our main file for our palette converter program. It contains all our flask modules since we will be using Flask
web application. This is where we will be asking the user to upload an image and then display the image with its palette.
The first route will accept the upload, send the upload to our extract_palette file to get the color values, and obtain the
hex values. The second route function will be used to display the results.

