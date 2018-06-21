import requests

def handle(req):
    
    r = requests.get('http://yoda-api.appspot.com/api/v1/yodish?text=' + req)

    result = r.json()

    return result["yodish"]
