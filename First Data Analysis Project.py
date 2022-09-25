#!/usr/bin/env python
# coding: utf-8

# In[12]:


import csv

with open('albumlist.csv', 'r') as file:
    reade = csv.DictReader(file)
    
    print(type(reade))
    print(reade.fieldnames)


# In[13]:


with open('albumlist.csv', 'r') as file:
    reade = csv.DictReader(file)
    
    for m in reade:
        print (m)


# In[16]:


with open('albumlist.csv', 'r') as file:
    reade = csv.DictReader(file)
    
    peter = 2
    for precious in reade:
        peter -= 1
        if (peter > 0):
            print(precious)
        else: 
            break


# In[8]:


import csv

with open('albumlist.csv', 'r') as file:
    reade = csv.DictReader(file)
    
    albums = []
    peter = 2
    for precious in reade:
        peter -=1
        albums.append(precious)
        if(peter > 0):     
            print(albums)
        else:
            break


# In[ ]:




