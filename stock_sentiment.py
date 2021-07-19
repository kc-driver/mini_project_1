import requests
from bs4 import BeautifulSoup

#scrape topglove comments
url = 'https://klse.i3investor.com/servlets/forum/800001345.jsp?ftp=400'
html = get(url)
sp = BeautifulSoup(html.text, 'html.parser')