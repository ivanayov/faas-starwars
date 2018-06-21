import os
from random import randint

def handle(req):
    images = os.listdir("function/pictures")

    index = randint(0, len(images)-1)
    with open("function/pictures/" + images[index], 'rb') as pic:
        jpgdata = pic.read()

    return jpgdata