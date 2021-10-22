#!/usr/bin/env python
# coding: utf-8

# # Exercici 1
# Crea una funció que donat un Array d’una dimensió, et faci un resum estadístic bàsic de les dades. Si detecta que l’array té més d’una dimensió, ha de mostrar un missatge d’error.

# In[12]:


import numpy as np

user = int(input("Cuantas dimensiones quieres crear en el array? "))

value = np.array([1,21,3,43,5,26,74,80,91,10], ndmin = user)

media = np.mean(value)
mediana = np.median(value)
percentil = np.percentile(value, 15)
desv_estandar = np.std(value)
varianza = np.var(value)
if user > 1:
    print("Error es un Array de mas de 1 dimension")
    print("Tiene {} dimensiones".format(value.ndim))
    print(value)
else: 
    print("Tiene {} dimension".format(value.ndim))
    print(value)

# resum estadístic bàsic de les dades.
print("")
print("La Media de nuestra matriz es: {}".format(media))
print("La Mediana de nuestra matriz es: {}".format(mediana))
print("El Percentil de 15 nuestra matriz es: {}".format(percentil))
print("La Desviación Estandar de nuestra matriz es: {}".format(desv_estandar))
print("La Varianza de nuestra matriz es: {}".format(varianza))


# In[ ]:





# In[ ]:




