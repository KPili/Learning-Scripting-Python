# This Python file uses the foloowing encoding: utf-8
from PIL import Image, ImageFilter

bulbasaur = Image.open('./Pokedex/bulbasaur.jpg')
pikachu = Image.open('./Pokedex/pikachu.jpg')

# Adding affects
sharp_plant = bulbasaur.filter(ImageFilter.SHARPEN)
turn_ninety_degrees = sharp_plant.rotate(90)
resize = bulbasaur.resize((100, 100))
crop_dimensions = (100, 100, 400, 400)
crop_pikachu = pikachu.crop(crop_dimensions)

# Saving to folder
sharp_plant.save("./altered_imgs/bulbaSORE.png", 'png')
turn_ninety_degrees.save("./altered_imgs/bulbaSORE90.png", 'png')
resize.save("./altered_imgs/smallasour.png", 'png')
crop_pikachu.save("./altered_imgs/crop.png", 'png')
# sharp_plant.show()
