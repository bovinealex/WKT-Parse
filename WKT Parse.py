#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import sys

#this is here because the size of the text file is so large
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


with open('multipolygons.txt', 'r') as AllWKT: 
    content = AllWKT.read()
def WKT_Parse (inputfile):
value = content
location = -1
end = []
start = []
while True:    #creates a list of end locations
    
    location = inputfile.find(")))", location + 1)
    if location == -1: break
    end.append(location)
    
    
while True:    #creates a list of start locations

    location = inputfile.find("MULTIPOLYGON", location + 1)
    if location == -1: break
    start.append(location)


# In[3]:



for i in range(len(start)):                     #will create individual multipolygon files for each of the sets stored in the larger file

    start_index = start[i]
    end_index = end[i]
    nameend = content.find('"MULT', end_index)    #basically the place where the next set of multipolygons starts
    name = content[end_index + 5:nameend]      #the name of the location is sotred between the end of one multipoly and the start of the other
    with open(name + '.txt', 'w') as myfile:
        myfile.write(content[start_index:end_index + 3])


# In[ ]:




