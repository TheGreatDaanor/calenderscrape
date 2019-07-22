from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

url='https://app.planning.nu/madurodam/madurodam-b.v./'
page = requests.get(url)


soup = BeautifulSoup(page.text,"html.parser")
#print(soup.prettify())

payload = {
    'xvalues[user]': 'dangelo',
    'xvalues[pass]': '',
    'submit':'login',
    'action':'submit'
}

with requests.session() as s:
    s.get(url)
    p = s.post('https://app.planning.nu/madurodam/madurodam-b.v./', data=payload)
#   print(p.text)

    r = s.get('https://app.planning.nu/madurodam/madurodam-b.v./rooster2/index2')
    print(r.text)
