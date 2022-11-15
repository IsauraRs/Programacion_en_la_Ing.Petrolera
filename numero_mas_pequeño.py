import numpy as np

#Buscando el número más pequeño antes de ser 0

a = 10

while(a!=0.0):

    a = a/10

    print("a = " , a)

print("El número más pequeño es: ", a)

#Operaciones entre números

a = 10
b = 2

while(b!=1):

    b = 1 - a / 10
    a = a / 10

print("el número más pequeño: con el que se hace la resta: ", a)

#Ejemplo de aplicación: Derivada

#f'(x)' = (f(x+h) - f(x)) / h | h --> 0

x = 2.0
h = 1e-07

fx = 2 * x ** 3
fxh = 2 * (x + h) ** 3

#Derivada analítica
fpx = 6 * x ** 2  
print("Derivada analítica: ", fpx)

#Derivada numérica
fpxn = (fxh - fx) / h  
print("Derivada numérica: " , fpxn)
