# This Python file uses the foloowing encoding: utf-8
from PIL import Image, ImageFilter

img = Image.open('./Pokedex/bulbasaur.jpg')
sharp_plant = img.filter(ImageFilter.SHARPEN)

turn_ninety_degrees = sharp_plant.rotate(90)
turn_ninety_degrees.save("./altered_imgs/bulbaSORE90.png", 'png')
sharp_plant.save("./altered_imgs/bulbaSORE.png", 'png')
# sharp_plant.show()
