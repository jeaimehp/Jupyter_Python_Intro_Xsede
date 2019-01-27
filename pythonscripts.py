#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/bin/python3
# Importing modules
import os
import numpy as np
import pandas as pd


# In[7]:


print("Checking for data directory and creating it if it is not there")
workingdir = os.getcwd() # get the current working directory  
print(workingdir)
try:
    os.stat("data")
except:
    print("data directory not found, making one")
    os.mkdir("data")
os.chdir("data")


# In[9]:


workingdir = os.getcwd()
print(workingdir)
print(os.listdir())


# In[23]:


print("Creating inital random dataset")
dataset = pd.DataFrame(np.random.randint(0,5000,size=(25,10)), columns=list('ABCDEFGHIJ'))
print(dataset.head())


# In[24]:


print("Creating converting to floats")
dataset = dataset / 1000
dataset.head()


# In[22]:


print("Statistical description of the dataset")
print(dataset.describe())


# In[25]:


print("saving the dataset to",workingdir,"/datafile.csv")
dataset.to_csv("datafile.csv")


# In[26]:


os.listdir()


# In[ ]:


print("Done")

