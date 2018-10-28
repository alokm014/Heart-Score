#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib.pyplot import plot, scatter, show
from numpy import NaN, Inf, arange, isscalar, asarray, array


# In[2]:


get_ipython().magic(u'matplotlib inline')


# In[3]:


df=pd.read_csv("Heart_Rate.csv")


# In[4]:


df.info()


# In[5]:


signal=df['Signal'].tolist()


# In[6]:


plot(signal)


# In[7]:


plot(signal[0:99])


# In[8]:


beat_count=0
maxtab=[]
for k in range(1,len(signal)-1):
    if(signal[k] > signal[k-1] and signal[k] > signal[k+1] and signal[k] > 1):
        maxtab.append(signal[k])
        beat_count= beat_count+1
        
N = len(signal)
fs = 100
duration_in_sec = N/fs
duration_in_min = duration_in_sec/60
BPM = beat_count/duration_in_min
print"Heart Rate:" +str(BPM)

