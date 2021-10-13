#!/usr/bin/env python
# coding: utf-8

# # Exercici 4
# 
# Implementa manualment una funció que calculi el coeficient de correlació. Informa’t-en sobre els seus usos i interpretació.

# In[6]:


import numpy as np

x = np.array([2, 4, 5, 7, 1])
y = np.array([7, 0, 8, 3, 9])

coeficient = np.corrcoef(x, y)
print(coeficient)

