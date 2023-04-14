#!/usr/bin/python3

"""TODO: Make the script executable
chmod +x imageConverter.py

Run script >> ./imageConverter.py"""

import os, sys
from PIL import Image


def convert_image():
    """ Open, Rotate, Resize and 
    Save an image in a specific format in a separate directory
    """
    
    # root/user/directory
    image_dir = "/home/wethinkcode/Pictures"
    path = os.listdir(image_dir)
    
    # iterate through the folder
    for oldName in path :
        file_name, ext = os.path.splitext(oldName)
        
        # convert to a new filename from jiff extension to jpeg extension
        newName = file_name + ".jpg"
        if (oldName != newName) and (oldName.endswith(".jiff")):
            try:
                with Image.open("/home/wethinkcode/Pictures/"+oldName) as im:
                    im = im.resize((128,128))\
                        .rotate(90).save("/home/wethinkcode/New/"+newName)
            except IOError:
                print("Cannot convert ", oldName)
        

convert_image() 