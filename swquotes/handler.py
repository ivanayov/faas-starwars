from random import randint

def handle(req):
    result = []

    for line in open("function/data.txt"):
        if req.lower() in line.lower():
            result.append(line)
    
    index = randint(0, len(result)-1)

    return result[index]
