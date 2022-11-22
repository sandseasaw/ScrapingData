#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4
import pandas as pd
import requests
import openpyxl
import re


# In[2]:


url = "https://www.eventseye.com/fairs/st1_trade-shows_jewelry.html"


# In[3]:


page = requests.get(url)


# In[4]:


soup = bs4.BeautifulSoup(page.text)


# In[5]:


events = soup.find('table',{'class':'tradeshows'})


# In[6]:


event = events.find('tbody')


# In[7]:


row = event.find_all('tr')


# In[8]:


name_list = []
information_list = []
location_list = []
date_list = []
cycle_list = []


# In[9]:


for c in row:
    name_list.append(c.find('td').find('a').find('b').text)
    
    information_list.append(c.find('td').find('a').find('i').text)
    
    location = c.find('a',{'class':'city'})
    location_list.append(location.text)


# In[10]:


tag = re.findall(r'<td>(.*?)</td>', page.text)
tag


# In[11]:


for l in range(0,50):
    cycle_list.append(tag[l*2])


# In[12]:


date_list = []
for k in range(1,100,2):
    date_list.append(tag[k])


# In[13]:


table = pd.DataFrame([date_list,name_list,location_list,information_list,cycle_list]).transpose()


# In[14]:


table.columns = ['date','name','location','information','cycle']


# In[15]:


table


# In[86]:


table.to_excel('events-all.xlsx',engine='openpyxl')

