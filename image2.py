from PIL import Image
im=Image.open("myimg.jpg")
myimg_gray=Image.open('myimg.jpg').convert('L')
myimg_gray.show()