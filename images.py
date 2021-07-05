from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

# Below applies various filters the source image above
filtered_img1 = img.filter(ImageFilter.BLUR)
filtered_img2 = img.filter(ImageFilter.SMOOTH)
filtered_img3 = img.filter(ImageFilter.SHARPEN)
filtered_img4 = img.convert('L')

# This saved a blurred image of the original pikachu.jpg (ImageFilter.BLUR)
filtered_img1.save("./altered_imgs/blur.png", 'png')

# This saved a smooth image of the original pikachu.jpg (ImageFilter.SMOOTH)
filtered_img2.save("./altered_imgs/smooth.png", 'png')

# This saved a sharpen image of the original pikachu.jpg (ImageFilter.SHARPEN)
filtered_img3.save("./altered_imgs/sharpen.png", 'png')

# This saves and covnerts a grey scale image of the original pikachu.jpg
filtered_img4.save("./altered_imgs/greyScale.png", 'png')
