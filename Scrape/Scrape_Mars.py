
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pymongo
import os
from splinter import Browser
import pandas as pd
import time


# In[3]:


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# In[4]:


db = client.craigslist_db
collection = db.items


# In[32]:


url = 'https://mars.nasa.gov/news/'

browser = Browser(driver_name="chrome")

# Retrieve page with the requests module
browser.visit(url)
response = browser.html

# Create BeautifulSoup object; parse with 'lxml'
soup = BeautifulSoup(response, 'lxml')


# In[36]:


# Find first news title
title = soup.find("div", {"class": "content_title"}).text
print("The first news title is: " + title)


# In[43]:


# Find first paragraph text

news_teaser = soup.find("div", {"class": "article_teaser_body"}).text
print("The paragraph text is: " + news_teaser)


# In[23]:


elem = soup.find("div", {"class": "article_teaser_body"})


# In[24]:


elem.attrs


# In[25]:


# Find image url for current featured image

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

browser = Browser(driver_name="chrome")

browser.visit(url)
response = browser.html

soup = BeautifulSoup(response, 'lxml')


# In[27]:


# featured_image_url
featured_image = soup.find("a", {"class": "button fancybox"})


# In[48]:


link = featured_image.attrs["data-fancybox-href"]
print("The image url is: https://www.jpl.nasa.gov" + link)

#full_link = 


# In[49]:


# Find latest tweet 

url = 'https://twitter.com/marswxreport?lang=ens'

browser = Browser(driver_name="chrome")

browser.visit(url)
response = browser.html

soup = BeautifulSoup(response, 'lxml')


# In[51]:


latest_tweet = soup.find("p", {"class": "TweetTextSize"}).text
print(latest_tweet)


# In[54]:


# Scrape the table containing facts about the planet including Diameter, Mass, etc
url = 'https://space-facts.com/mars/'

browser = Browser(driver_name="chrome")

browser.visit(url)
response = browser.html

soup = BeautifulSoup(response, 'lxml')


# In[72]:


#Grab table

url = 'https://space-facts.com/mars/'

mars_table = pd.read_html(url, header=0)
mars_table[0]


# In[20]:


#Find high-res images

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser = Browser(driver_name="chrome")

browser.visit(url)
response = browser.html

soup = BeautifulSoup(response, 'lxml')


# In[21]:


highres_image = soup.find_all("a", {"class": "itemLink product-item"})
print(highres_image)
#len(highres_image)


# In[23]:


highres_image[1].text


# In[26]:


#Grab hemisphere image urls and store in dictionary

hemisphere_image_urls = []

for i in range (1,8,2):
    image = highres_image[i]

    link1 = "https://astrogeology.usgs.gov" + image.attrs["href"]
    title = image.text
    browser = Browser(driver_name="chrome")

    browser.visit(link1)
    response = browser.html

    soup = BeautifulSoup(response, 'lxml')
    
    images = soup.find_all("a")

    for image in images: 
        if image.text == "Sample":
            image_url = image.attrs["href"]
            break
    hemisphere_image_urls.append({"title": title, "image_url": image_url})
    


# In[27]:


print(hemisphere_image_urls)

