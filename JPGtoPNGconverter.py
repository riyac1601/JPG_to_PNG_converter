import sys
import os
from PIL import Image

# grab first and second argument
path = sys.argv[1]
directory = sys.argv[2]

# check if \new exists , if not create it
if not os.path.exists(directory):
    os.makedirs(directory)

# loop through Pokedex
# convert to png
# save to \new folder
for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{path}{filename}')
    img.save(f'{directory}/{clean_name}.png', 'png')
    print('all done!')
    
# access it in cmd line as : 
# python JPGtoPNGconverter.py Pokedex\ new\

