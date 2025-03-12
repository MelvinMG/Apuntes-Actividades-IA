import cv2
import numpy as np
"""
Este es un ejemplo sencillo de como cargar una imagen en escala de grises con OpenCV
y mostrarla en una ventana.
"""

img = cv2.imread('Ejemplos/Ejemplo_OpenCV/ejemplo.png')# Cargamos la imagen en escala de grises,dandole una ruta de la imagen
imgn= np.zeros(img.shape[:2], np.uint8) # Creamos una imagen en escala de grises con las mismas dimensiones que la imagen original

# se puede manipular el tono en mgn= np.zeros(img.shape[:2],np.unit8)*150(eso es un tono gris) o *255(eso es un tono blanco)

"""
Se mostrara la imagen sobre encima de la ventana llamada 'salida'
"""
#img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)# Convertimos la imagen a escala de grises
#img3=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)# Convertimos la imagen a escala de RGB
#img4=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)# Convertimos la imagen a escala de HSV
"""
Con los modelos de color podemos hacer diferentes operaciones con las imagenes
como por ejemplo cambiar el brillo, contraste, saturacion, etc
"""

r,g,b=cv2.split(img)# Separamos los canales de la imagen
imgb=cv2.merge((b,imgn,imgn))
imgr=cv2.merge((imgn,g,imgn))
imgg=cv2.merge((imgn,imgn,g))


print(img.shape)# imprimimos los valores de la imagen

cv2.imshow('salida1', img)# Mostramos la imagen 
cv2.imshow('salida2', img)# Mostramos la imagen en escala de grises
#cv2.imshow('salida3', img2)# Mostramos la imagen en escala de grises
#cv2.imshow('salida4', img3)# Mostramos la imagen en escala de RGB
#cv2.imshow('salida5', img4)# Mostramos la imagen en escala de HSV

#cv2.imshow('salida escala rojo', r)# Mostramos el canal rojo
#cv2.imshow('salida escala verde', g)# Mostramos el canal verde  
#cv2.imshow('salida escala azul', b)# Mostramos el canal azul

#cv2.imshow('salida con escala negros', imgn)# Mostramos la imagen en escala negros
cv2.imshow('salida con escala azul', imgb)# Mostramos la imagen en escala azul
cv2.imshow('salida con escala verde', imgr)# Mostramos la imagen en escala verde
cv2.imshow('salida con escala rojo', imgg)# Mostramos la imagen en escala rojo


cv2.waitKey(0)# Esperamos a que se presione una tecla


cv2.destroyAllWindows()# Cerramos todas las ventanas