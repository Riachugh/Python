#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


# In[7]:


df = pd.read_csv('C:/Users/LENOVO/Downloads/Cars.csv')


# In[8]:


df


# In[8]:


import scipy
import numpy as np


# In[9]:


from scipy.stats import norm


# In[10]:


val,m,s = 38,34.4,9.1


# In[11]:


print(norm.cdf(val,m,s))


# In[12]:


print(1-norm.cdf(val,m,s))


# In[13]:


val,m,s = 40,34.4,9.1


# In[14]:


print(norm.cdf(val,m,s))


# In[18]:


print(norm.cdf(50,34.4,9.1)-(norm.cdf(20,34.4,9.1)))


# In[ ]:




