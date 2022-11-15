import numpy as np
import matplotlib.pyplot as plt

#Creando el vector de la variable independiente 
x = np.linspace(0 , 5 , 20)
fx = 3 + x ** 2.0
h = 1e-03 
#Derivada numérica mediante la definición
fxp = ((3 + (x + h) ** 2.0) - (3 + x ** 2.0)) / h
#Derivada analítica
fxpa = 2 * x
print("Derivada analítica = " ,fxpa)
print("Derivada numérica = " ,fxp)

#Haciendo una recta secante 
c = np.array([x[4] , x[16]])
fc = np.array([fx[4] , fx[16]])

#Función original
plt.plot(x , fx) 
#Secante
plt.plot(c , fc , 'or--') 
#Derivada, está lejos por la constante
plt.plot(x , fxp, 'b-.')
plt.show()


