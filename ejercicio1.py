# -*- coding: utf-8 -*-
"""
Created on Wed May  5 15:50:36 2020

@author: MILAGROS PC
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('contr2.jpg')

#realizmos el histograma de la imagen original 
histOriginal = cv2.calcHist([imagen], [0], None, [256], [0, 256])

plt.plot(histOriginal, color = 'black')
plt.xlabel('Intensidad de iluminacion')
plt.ylabel('Cantidad de pixeles')
plt.show()

imagen_original = cv2.imread('contr2.jpg')
imagen_resultado = cv2.imread('contr2.jpg')

# Convertir las imágenes del formato BGR a RGB porque matplotlib acepta 
# imagenes en formato RGB 
imagen_original = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2RGB)
imagen_resultado = cv2.cvtColor(imagen_resultado, cv2.COLOR_BGR2RGB)


#Detallamos los valores de las variables de Contrast stretching 
a = 0   # límite inferior
b = 255 # límite superior
#c = 69
#d = 149
c = np.min(imagen_original)  # El menor valor de los pixeles
d = np.max(imagen_original)  # El mayor valor de los pixeles


alto, ancho, canales = imagen_original.shape 

def point_operator(pixel_RGB):
    return (pixel_RGB - c) * ((b - a) / (d - c) + a)

for x in range(alto):
    for y in range(ancho):
        imagen_resultado[x][y] = point_operator(imagen_original[x][y])
        
        
        
# Mostrar la imágen luego de aplicar el algoritmo 
# del mapeo lineal punto a punto
plt.imshow(imagen_resultado)

#Guardamos la imagen
plt.savefig("imagen_resultado_salida.jpg", bbox_inches='tight')


