
""" El error que tenia el codigo por el cual no funcionaba 
la ejecucion era que le faltabala importacion del 
numpy(se especializa en el calculo numerico y el analisis de datos)"""

import numpy as np
from scipy import ndimage # permite procesamiento y analisis de imagenes que están diseñadas para operar con matrices de dimensionalidad arbitraria
import matplotlib.pyplot as plt #biblioteca para la generación de gráficos a partir de datos contenidos en listas o arrays

im = np.zeros((256, 256)) # crea una matriz de de 256 por 256 llegana de ceros y la guarda en im
im[64:-64, 64:-64] = 1 # a ese rango de x e y de la matriz asignele 1

im = ndimage.rotate(im, 15, mode='constant') # la mtriz se gira 15 grados y el modo constante le da bordes
im = ndimage.gaussian_filter(im, 8) # le da un filtro a la matriz

sx = ndimage.sobel(im, axis=0, mode='constant') # calcula un filtro para la matriz de entrada y se guarda en una variable
sy = ndimage.sobel(im, axis=1, mode='constant') # calcula un filtro para la matriz de entrada y se guarda en una variable
sob = np.hypot(sx, sy) # saca la hipotenusa entre los dos filtros(matrices) creados anteriormente

plt.figure(figsize=(16, 5)) # crea un contenedor de nivel superior para todos los elementos de la trama
plt.subplot(141) #crear una figura en una misma ventana
plt.imshow(im, cmap=plt.cm.gray) # muestra la matriz im
plt.axis('off') # quita la escala de la grafica
plt.title('square', fontsize=20) # dar titulo a la figura creada
plt.subplot(142) #crear una figura en una misma ventana
plt.imshow(sx) # muestra la matriz sx 
plt.axis('off') # quita la escala de la grafica
plt.title('Sobel (x direction)', fontsize=20) # dar titulo a la figura creada
plt.subplot(143) #crear una figura en una misma ventana
plt.imshow(sob) # muestra la matriz sob
plt.axis('off') # quita la escala de la grafica
plt.title('Sobel filter', fontsize=20) # dar titulo a la figura creada

im += 0.07*np.random.random(im.shape) # genera una nueva matriz utilizando la matriz ya creada y multiplicando 0.07 de forma random a la matriz

sx = ndimage.sobel(im, axis=0, mode='constant') # calcula un filtro para la matriz nueva y se guarda en una variable
sy = ndimage.sobel(im, axis=1, mode='constant') # calcula un filtro para la matriz nueva y se guarda en una variable
sob = np.hypot(sx, sy) # saca la hipotenusa entre los dos filtros(matrices) creados anteriormente

plt.subplot(144) #crear una figura en una misma ventana
plt.imshow(sob) # muestra la matriz sob nueva
plt.axis('off') # quita la escala de la grafica
plt.title('Sobel for noisy image', fontsize=20) # dar titulo a la figura creada



plt.subplots_adjust(wspace=0.02, hspace=0.02, top=1, bottom=0, left=0, right=0.9) # margen a cada figura

plt.show() # muestra lo que se codifico