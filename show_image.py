# This Python file uses the foloowing encoding: utf-8
from PIL import Image, ImageFilter

img = Image.open('./Pokedex/bulbasaur.jpg')

# Adding affects
sharp_plant = img.filter(ImageFilter.SHARPEN)
turn_ninety_degrees = sharp_plant.rotate(90)
resize = img.resize((100, 100))

# Saving to folder
sharp_plant.save("./altered_imgs/bulbaSORE.png", 'png')
turn_ninety_degrees.save("./altered_imgs/bulbaSORE90.png", 'png')
resize.save("./altered_imgs/smallasour.png", 'png')
# sharp_plant.show()
