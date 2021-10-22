#!/usr/bin/env python
# coding: utf-8

# # Exercici 2
# 
# Crea una funció que et generi un quadrat NxN de nombres aleatoris entre el 0 i el 100.

# In[2]:


import numpy as np
import random

user = int(input("Hey Hola, dime un numero para crearte una dimensión NxN: "))
num = np.random.randint(0, 100,(user, user))

print(num)


# In[ ]:





# In[ ]:




