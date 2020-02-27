#!/usr/bin/env python
# coding: utf-8

# In[61]:


import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis

import time


# In[4]:


plt.rcParams["figure.figsize"] = 64, 64


# In[55]:


#Iteration count
def Iteration_count(c,threshold):
    z = complex(0, 0)
    for iteration in range(threshold):
        z = z**2 + c
        if abs(z) > 4:
            break
    return iteration

def mandelbrot(threshold, img_size=1000):
    r_Axis = np.linspace(-2,1, img_size)
    i_Axis = np.linspace(-1.5,1.5, img_size)
     plot = np.empty((r_Axis.size, i_Axis.size))
     
    for index_x,ix in enumerate(r_Axis):
        for index_y,iy in enumerate(i_Axis):
            plot[index_x, index_y] = Iteration_count(complex(ix, iy), threshold)
    return plot
    
def save_img(arr):
    plt.imshow(arr.T, interpolation="nearest")
    plt.savefig("mandel.jpg", dpi=300)


# In[66]:


t0 = time.time()
out = mandelbrot(50, 1000)
t1 = time.time()


# In[67]:


t1-t0


# In[68]:


plt.imshow(out.T)
plt.show()


# In[57]:


save_img(out)


# In[ ]:




