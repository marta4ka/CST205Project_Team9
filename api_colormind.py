import requests
import json
import random
#=========================================================================
#the function getFivePalettes is the only thing we need out of this doc
#=========================================================================

def getFirstPalette(image):

    from colorthief import ColorThief
    color_thief = ColorThief(image)

    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)

    #creating a varible named palette, it contains the 4 main colors
    palette = color_thief.get_palette(color_count=6)

    return(palette)

def getSecondPalette(image):

    from colorthief import ColorThief
    color_thief = ColorThief(image)

    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)

    #creating a varible anmed palette, it contains the 4 main colors
    palette = color_thief.get_palette(color_count=6)
    return(palette)

#to generate the 5 palettes, we are creating a for loop that runs 5 times
def getFivePalettes(image):

    Pal1 = getFirstPalette(image) #list of rgb values in most used colors
    Pal2 = getSecondPalette(image) #list of rgb values in most used colors

    num = 0

    fivePalettes = []
    for i in range(5):
        #we are taking a random tuple from the palette, and setting each value to a varible, RGB for cocatination in data
        #each block represents one tuple
        R1 = str(Pal1[num][0])
        G1 = str(Pal1[num][1])
        B1 = str(Pal1[num][2])

        R2 = str(Pal2[num+1][0])
        G2 = str(Pal2[num+1][1])
        B2 = str(Pal2[num+1][2])
        url = 'http://colormind.io/api/'

        #this data takes the generated values in our two tuples, and sets it to readable data for the api
        data = '''{"input":[[''' + R1 + ''',''' + G1 + ''',''' + B1 + '''],[''' + R2 + ''',''' + G2 + ''',''' + B2 + '''],"N","N","N"],
           "model": "default"
         }'''

        #api stuff
        bin_data = data.encode('ascii')
        response = requests.post(url, data=bin_data)

        # For successful API call, response code will be 200 (OK)
        if(response.ok):

            # Loading the response data into a dict variable
            # json.loads takes in only binary or string variables so using content to fetch binary content
            # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
            jData = json.loads(response.content.decode('ascii'))

            #jDta will be returning(for now, printing) 5 lists, which can be used in the webpage for display purposes, jData what we will be working with
            #print(jData["result"])
            fivePalettes.append(jData["result"])

        else:
          # If response code is not ok (200), print the resulting http error code with description
            myResponse.raise_for_status()
        num = num + 1
    return fivePalettes
