import requests

URL = "https://www.basketball-reference.com/players/a/abdulka01.html"
page = requests.get(URL)

print(page.text)