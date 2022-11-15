import numpy as np 
import time 
from math import pi

size = 100

A1 = np.arange(size)
A2 = np.arange(size)

print(A1)
print(A2)

a = np.arange(15 , 30 , 1.0)
print(a)

#No se pueden hacer arreglos al revés
#a = np.arange(30 , 15 , 1.0).reshape(5 , 3)

#Para hacerlo, poner número negativo en el salto
a = np.arange(30 , 15 , -1.0).reshape(5 , 3)
print(a)

a = np.transpose(a)
print("aT = " , a)

print(a.shape)

print(a.ndim)

#Tipo de dato
print(a.dtype.name)

print(a.itemsize)

#Número de datos
print(a.size)

i = np.array([2 , 3 , 4 , 19 , 23 , 39 , 39])
print("i = ", i)

#Con números complejos
b1 = np.array([1 + 1j , 3 + 5j , 5 - 8j] , dtype= np.complex128)
b2 = np.array([3 + 1j , 4 + 5j , 18 - 8j] , dtype = np.complex128)

print( b1  + b2)

c = np.array( [ [1 , 2] , [3 , 4]])
print(c.dtype)

#Hipermatriz
d = np.zeros((10 , 4 , 3))
print("Matriz de ceros: " , d)

e = np.ones((10 , 3 , 4))
f = np.empty((2 , 3))
print("Matriz vacía: " , f)

g = np.arange(3 , 2.1 , -0.12)
print("Imprime un rango de valores: " , g)

h= np.linspace(65.3 , 2.39391 , 9)
print("Imprime un espacio lineal: " , h)

print("Imprime el número en el índice  0: " , h[1])