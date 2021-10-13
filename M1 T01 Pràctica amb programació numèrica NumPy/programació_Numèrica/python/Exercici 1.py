#!/usr/bin/env python
# coding: utf-8

# # Exercici 1
# Crea una funció que donat un Array d’una dimensió, et faci un resum estadístic bàsic de les dades. Si detecta que l’array té més d’una dimensió, ha de mostrar un missatge d’error.

# In[4]:


import numpy as np

user = int(input("Cuantas dimensiones quieres crear en el array?"))

value = np.array([1,2,3,4,5,6,7,8,9,10], ndmin = user)
if user > 1:
    print("Error es un Array de mas de 1 dimension")
    print("Tiene {} dimensiones".format(value.ndim))
    print(value)
else: 
    print("Tiene {} dimension".format(value.ndim))
    print(value)


# In[ ]:




