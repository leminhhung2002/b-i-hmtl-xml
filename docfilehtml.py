from bs4 import BeautifulSoup
import requests
url = requests.get("https://leminhhung2002.github.io/-valentine-Lan-/")
Soup= BeautifulSoup(url.content,"lxml")
hung = Soup.find_all(True,limit=1)
for i in hung:
    print(i.text)
