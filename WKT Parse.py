#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import sys

#this is here because the size of multipolygon text files are often larger than what is typicallt handals
#it basically circumvents the field limit error that arises when a file this large is used
maxInt = sys.maxsize
decrement = True

while decrement:

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:            
        maxInt = int(maxInt/10)
        decrement = True


# In[2]:

#the multipolygons.txt file used as an example cointains two polygons, which outline adminstravie boundaries in Indonesia
with open('multipolygons.txt', 'r') as AllWKT: 
    content = AllWKT.read()
value = content
location = -1
end = []
start = []
while True:    
#creates a list of end locations
    location = inputfile.find(")))", location + 1)
    if location == -1: break
    end.append(location)
    
    
while True:    
#creates a list of start locations
    location = inputfile.find("MULTIPOLYGON", location + 1)
    if location == -1: break
    start.append(location)


# In[3]:



for i in range(len(start)):                     
#will create individual multipolygon files for each of the sets stored in the larger file
    start_index = start[i]
    end_index = end[i]
    nameend = content.find('"MULT', end_index)    
    name = content[end_index + 5:nameend]      
    with open(name + '.txt', 'w') as myfile:
        myfile.write(content[start_index:end_index + 3])





