#!/usr/bin/env python
# coding: utf-8

# In[17]:


greet = lambda name : print(f"Good Morning {name}")


# In[19]:


greet("Ravi")

product = lambda a,b,c : a*b*c
# In[21]:


product(10,20,30)


# In[23]:


product = lambda a,b,c : a*b*c


# In[25]:


product(10,20,30)


# In[27]:


even = lambda L : [x for x in L if x%2 == 0]


# In[29]:


my_list = [100,3,9,38,43,56,20]
even(my_list)


# In[39]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter + 1
        sum += x
    mean = sum/counter
    return mean


# In[43]:


mean_value(5,7,8,9,10)


# In[33]:


def product (*n):
    result = 1
    for i in range(len(n)):
        result *= n[i]
    return result


# In[37]:


product(5,9,8)


# In[45]:


import compute


# In[47]:


compute.mean_value


# In[ ]:




