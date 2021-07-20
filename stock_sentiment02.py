from selenium import webdriver
from bs4 import BeautifulSoup
import chromedriver_binary
import pandas as pd


user=[]
date=[]
comt=[]

def my_scrape():
    for li in list_sp:
        name_sp = li.find('span',attrs={'class':'comuid'})
        print(name_sp.text)
        user.append(name_sp.text)

        date_sp = li.find('span',attrs={'class':'comdt'})
        print(date_sp.text)
        date.append(date_sp.text)

        comment_sp = li.find('span',attrs={'class':'autolink'})
        if comment_sp!=None:
            #print(comment_sp)
            comt.append(comment_sp.text)
        else:
            #print('Removed')
            comt.append(comment_sp)

            
driver = webdriver.Chrome()
page = 400
root ='https://klse.i3investor.com/servlets/forum/800001345.jsp?ftp='
#concatenate str with int url
tglove = root + str(page)

# get the data
driver.get(tglove)

# load data into bs4
soup = BeautifulSoup(driver.page_source,'html.parser')
list_sp = soup.find_all('td',attrs={'style':'word-wrap: break-word;'})

for page in range(400,403):
    my_scrape()
    page += 1
    tglove = root + str(page) #goto next page
        
klse_dict = {'Date': date,'Username': user,'Comment': comt}
klse_sentiment = pd.DataFrame(klse_dict)
print(klse_sentiment)
klse_sentiment.to_csv('klse_sentiment.csv',index=False)