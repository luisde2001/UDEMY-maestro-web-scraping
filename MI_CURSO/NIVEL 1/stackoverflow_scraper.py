import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
}

url = "https://stackoverflow.com/questions"

respuesta = requests.get(url, headers=headers)

soup = BeautifulSoup(respuesta.text)
