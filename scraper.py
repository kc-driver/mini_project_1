#klse stock comment scraper at https://klse.i3investor.com/ for Top Glove counter
#iteration in a range + save as csv file at specific path

from selenium import webdriver
from bs4 import BeautifulSoup
import chromedriver_binary
import pandas as pd
import time
import os

user=[]
date=[]
comt=[]


def my_scrape():
    for li in list_sp:
        name_sp = li.find('span',attrs={'class':'comuid'})
        #print(name_sp.text)
        user.append(name_sp.text)

        date_sp = li.find('span',attrs={'class':'comdt'})
        #print(date_sp.text)
        date.append(date_sp.text)

        comment_sp = li.find('span',attrs={'class':'autolink'})
        if comment_sp!=None:
            comt.append(comment_sp.text)
        else:
            comt.append(comment_sp)

  

page = 400
root ='https://klse.i3investor.com/servlets/forum/800001345.jsp?ftp='
#concatenate str with int url
tglove = root + str(page)
driver = webdriver.Chrome()
path = r'c:\Users\User\Desktop\mini project 1'
driver.get(tglove)

for page in range(400,2750):
    soup = BeautifulSoup(driver.page_source,'html.parser') # load data into bs4
    list_sp = soup.find_all('td',attrs={'style':'word-wrap: break-word;'})
    my_scrape()
    klse_dict = {'Date': date,'Username': user,'Comment': comt}
    df = pd.DataFrame(klse_dict)
    if os.path.isfile('senti.csv') == True:
        df.to_csv('senti.csv',mode='a',index=False,header=False)
    else:
        df.to_csv('senti.csv',index=False)
    page += 1
    tglove = root + str(page) #goto next page
    driver.get(tglove)
    user.clear()
    date.clear()
    comt.clear()
    #time.sleep(2)

driver.close()