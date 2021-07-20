from selenium import webdriver
from bs4 import BeautifulSoup
import datetime

#open page
driver = webdriver.Chrome()
url='https://klse.i3investor.com/servlets/forum/800001345.jsp?ftp=400'
driver.get(url)

#bs4 container
soup = BeautifulSoup(driver.page_source,'html.parser')
list_sp = soup.find_all('td',attrs={'style':'word-wrap: break-word;'})


user=[]
date=[]
comt=[]

for li in list_sp:
    name_sp = li.find('span',attrs={'class':'comuid'})
    print(name_sp.text)
    user.append(name_sp)

    date_sp = li.find('span',attrs={'class':'comdt'})
    print(date_sp.text)
    date.append(date_sp)

    comment_sp = li.find('span',attrs={'class':'autolink'})
    if comment_sp!=None:
        print(comment_sp.text)
        comt.append(comment_sp)