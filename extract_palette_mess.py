"""
File Name: extract_palette.py
Team N9ne: Herendira Camarillo, Marta Gubanova, Jose Morado, Marco Rosales
Date: 5/10/2019
Description:  This file takes an image and analyzes the image to extract its
              color values. It will then put the colors from the image into
              seperate boxes and then will place them sequentially and
              horizontally on a blank canvas. When the canvas is created we
              will have two examples: a palette with the colors in the image,
              and the original image with the palette beneath it.
"""
#we first import pillow module so that we can be able to manipulate image
from PIL import Image, ImageDraw
#we will also be converting our rgb values to hex values
from webcolors import rgb_to_hex
#This function will be used to get the number of colors in the image
#so that we can extract each one and create a palette with the specified colors.
import api_colormind
#this file is used to access a function taking main colors from the image and generating a complementary palette using API.

def extract_colors(image, outline_width, outline_color, color_count=5):
    #we grab the original image that the user uploaded and open it
    initial_image = Image.open(image)
    #then we figure out the dimensions of the uploaded image
    width, height = initial_image.size
    #use API to generate a new palette using the main colors in the image
    list_of_colors = api_colormind.getFivePalettes(image)
    #then we print the type of our color object i.e. <class 'list'>
    print(type(list_of_colors))
    #this value will be used to assign the sampled colors size so we can
    #create the sequence of colors in the palette
    sampled_colors_size = 100
    #and create the dimensions for our palette
    palette_height = int(height/palette_length_div)
    #Here we create a blank canvas that will use to draw(print) the new image with palette
    canvas = Image.new("RGB", (width, height + palette_height))   # blank canvas(original image + palette)
    image_with_palette_caption = Image.new("RGB", (width, palette_height))
    #and then we create the palette image just by itself
    palette = Image.new("RGB", (color_count*sampled_colors_size, sampled_colors_size))
    #we use ImageDraw Module to create a new image with our palette displayed
    palette_below_image = ImageDraw.Draw(image_with_palette_caption)
    #and then we use it again to display the palette only
    pure_palette = ImageDraw.Draw(palette)
    #we give our new images an x coordinate of 0 so that they can be placed
    #on the webpage
    position_image_with_palette = 0
    position_pure_palette = 0
    #We reduce the size of the width of the palette to fit our webpage screen
    sampled_palette_size = width/5
    #create a list for our hex values
    hex_values = []
    #this loop wil create the palette, it will go through each of the 5 colors
    #and will place each color in a rectangle box and place them all sequentially
    #together in a horizontal direction
    for i in range(5):
        unique_color = tuple(list_of_colors[0][i])
        #create palette to be placed below image
        palette_below_image.rectangle([position_image_with_palette, 0, position_image_with_palette + sampled_palette_size, palette_height], fill=unique_color, width=outline_width, outline=outline_color)
        #create the palette that will be displayed at the bottom of the webpage
        pure_palette.rectangle([position_pure_palette, 0, position_pure_palette+sampled_colors_size, sampled_colors_size], fill=unique_color)
        #we specify where to place the image with palette
        position_image_with_palette = position_image_with_palette + sampled_palette_size
        #and where to place the palette
        position_pure_palette = position_pure_palette + sampled_colors_size
        #display the hex values for each beneath the specified color
        hex_values.append(rgb_to_hex(unique_color[:3]))
    #we then delete these objects so that the program is refreshed when we go back to main page
    del palette_below_image
    del pure_palette
    #tuple with specified dimensions for one of our images.
    customized_canvas = (0, height, width, height + palette_height)
    #finally we put the results on the canvas to be displayed
    canvas.paste(initial_image)
    canvas.paste(image_with_palette_caption, customized_canvas)
    #displays the the results i.e. palette and palette with image above it
    return canvas, palette, hex_values