#!/usr/bin/env python
# coding: utf-8

# # Exercici 2
# 
# Crea una funció que et generi un quadrat NxN de nombres aleatoris entre el 0 i el 100.

# In[21]:


import numpy as np
import random
num = np.random.randint(0, 100, (10, 10))

print(num)

