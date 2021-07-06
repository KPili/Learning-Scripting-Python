# This Python file uses the foloowing encoding: utf-8
from PIL import Image, ImageFilter

img = Image.open('./Pokedex/bulbasaur.jpg')
sharp_plant = img.filter(ImageFilter.SHARPEN)

sharp_plant.save("./altered_imgs/bulbaSORE.png", 'png')
sharp_plant.show()
