import os
from random import randint
from PIL import Image

def handle(req):
    images = os.listdir("pictures")

    index = randint(0, len(images)-1)
    img = Image.open('pictures/' + images[index])
    img.show()

    return img
