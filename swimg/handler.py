import os, sys
from random import randint

def handle(req):
    images = os.listdir("function/pictures")

    if req:
        name = req.lower().replace(" ", "_")
        matching = [s for s in images if name in s]
        if len(matching):
            index = randint(0, len(matching)-1)
            with open("function/pictures/" + matching[index], 'rb') as pic:
                res = pic.read()
        else:
            res = "Image is not available"
    else:
        index = randint(0, len(images)-1)
        with open("function/pictures/" + images[index], 'rb') as pic:
            res = pic.read()
        
    os.write(1, res)
    return res