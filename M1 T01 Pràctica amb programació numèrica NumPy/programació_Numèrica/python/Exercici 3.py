#!/usr/bin/env python
# coding: utf-8

# # Exercici 3
# 
# Crea una funció que donada una taula de dues dimensions, et calculi els totals per fila i els totals per columna.  

# In[5]:


import numpy as np

num = np.array([[12,3,1,4],[55,2,6,9]])
suma = np.sum(num, axis = 0)
print(suma)


# In[ ]:




