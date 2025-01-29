
#Earbuds

import bs4
from bs4 import BeautifulSoup as bs
import requests
link="https://www.amazon.com/All-New-release-Smart-speaker-Charcoal/dp/B09B8V1LZ3?th"
page=requests.get(link)
page
page.content
## now let us parse the html page
soup=bs(page.content,'html.parser')
print(soup.prettify())
#when you parse HTML using BeautifulSoup, you are converting the 
#raw HTML content of a web page into a structured format, 
#like a tree, where you can easily locate and manipulate individual 
#elements (such as tags, attributes, or text).
soup
#page.content=> provides the raw HTML content,
#while soup.prettify()=> offers a formatted, human-readable version of the parsed HTML content.

## now let us scrap the contents
names=soup.find_all('span',class_="a-spacing-small")
names

### but the data contains with html tags,let us extract names from html tags
cust_names=[]
for i in range(0,len(names)):
    cust_names.append(names[i].get_text())
    
cust_names
len(cust_names)
#cust_names.pop(-1)
#len(cust_names)


### There are total 6 users names 
#Now let us try to identify the titles of reviews

title=soup.find_all('b',class_="a-letter-space")
title
# when you will extract the web page got to all reviews rather top revews.when you
# click arrow icon and the total reviews ,there you will find span has no class
# you will have to go to parent icon i.e.a
#now let us extract the data
review_titles=[]
for i in range(0,len(title)):
    review_titles.append(title[i].get_text())
review_titles

len(review_titles)
##now let us scrap ratings
rating=soup.find_all('span',class_="a-icon a-icon-popover__rating")
rating
###we got the data
ratings = [int(span['data-score']) for span in soup.find_all('span', {'class': 'a-icon a-icon-popover__rating'})]

# Print the ratings
print(ratings)

len(ratings)



## now let us scrap review body
reviews=soup.find_all("div",class_="a-icon a-icon-popover__body")
reviews
review_body=[]
for i in range(0,len(reviews)):
    review_body.append(reviews[i].get_text())
review_body
review_body=[ reviews.strip('\n\n')for reviews in review_body]
review_body
len(review_body)

##########################################
###convert to csv file
import pandas as pd
df=pd.DataFrame()
df['customer_names']=cust_names
df['review_title']=review_titles
df['rate']=ratings
df['review_body']=review_body
df
df.to_csv('C:\8-textmining\Web.py',index=True)
########################################################
#sentiment analysis
import pandas as pd
from textblob import TextBlob
df=pd.read_csv("C:/8-textmining/Web.py")
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
