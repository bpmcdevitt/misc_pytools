#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import sys

url = sys.argv[1]
r  = requests.get('http://' +url)
data = r.text
soup = BeautifulSoup(data, 'lxml')

for link in soup.find_all('a'):
            print(link.get('href'))

for link in soup.find_all('img'):
            print(link.get('src'))
