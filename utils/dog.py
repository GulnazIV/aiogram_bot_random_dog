import requests

def random_dog():
    dog = requests.get("https://random.dog/woof.json").json()
    return dog['url']
