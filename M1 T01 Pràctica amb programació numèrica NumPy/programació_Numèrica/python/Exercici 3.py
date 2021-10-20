#!/usr/bin/env python
# coding: utf-8

# # Exercici 3
# 
# Crea una funció que donada una taula de dues dimensions, et calculi els totals per fila i els totals per columna.  

# In[2]:


import numpy as np

num = np.array([[12,3,1,4],[55,2,6,9]])
suma_fila = np.sum(num, axis = 0)
suma_columna = np.sum(num, axis = 1)
print("Filas: {}".format(suma_fila))
print("Columnas: {}".format(suma_columna))


# In[ ]:




