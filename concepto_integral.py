import numpy as np
import matplotlib.pyplot as plt

#Número de particiones
n_part = 100 
#Valor izquierdo para el intervalo cerrado
a = -3.0
#Valor derecho para el intervalo cerrado
b = 3.0
#Se crea el vecto del intervalo
x = np.linspace(a , b , n_part)
#f(x)
f = x ** 3.0
#Integral analítica
int_f = (b ** 4.0 / 4.0 - a ** 4.0 / 4)
#Suma comienza en cero
suma = 0.0

for i in range(0 , n_part - 1):

    #Cálculo de la base
    delta_x = x[i + 1] - x[i]
    #Cálculo de la altura
    f_x = x[i + 1] ** 3.0
    suma = suma + f_x * delta_x
    #Coordenadas en x y y de los rectángulos
    xc = [x[i] , x[i] , x[i + 1] , x[ i + 1]]
    yc = [0 , f_x , f_x , 0]

    plt.fill(xc , yc , 'b' , edgecolor = 'k' , alpha = 1.0)

plt.plot(x , f , 'r-' , label = "f(x)")
plt.legend()
plt.grid()
plt.show()
print("El área bajo la curva de la función es: " , round(abs(suma) , 7))
print("Integral exacta: " , int_f , "Integral numérica: " , suma)