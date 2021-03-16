#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
x=input ("Потери=")
x=int(x)
y=input ("Прибыль=")
y=int(y)
if x>y:
    res=x-y
    print ("Ваши убытки составили:",res)
elif x<y:
    res=y-x
    print ("Ваши прибыль составили:",res) 


# In[ ]:




