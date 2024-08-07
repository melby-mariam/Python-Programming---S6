from PIL import Image
im=Image.open("myimg.jpg")
im.save("Melby.png")
im.thumbnail((300,300))
im.show()