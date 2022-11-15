'''
Se parte de una condición inicial 
Cuando se toman mallas muy pequeñas se usan coordenadas radiales
Coordenadas cilíndricas: 
Se tiene derivada temporal se aplica discretización de Euler hacia atrás (p ^(n + 1) - p ^ n) / deltat
Se relaciona el tiempo actual con el anterior
alpha/h deltaP/deltat = delta^2P/deltax^2
alpha / h = C
C * (p ^(n + 1) - p ^ n) / deltat = (P(i + 1) - 2Pi + P(i-1) / deltax^2)^n
Si se evalúa en el tiempo anterior se usa un esquema explícito en el tiempo
Sol.Explícita del flujo monofásico unidimensional transitorio:
Pi ^ (n+1) = ((P(i + 1) - 2Pi + P(i-1)) / deltax^2) * (deltat/C) + Pi ^ n
Pin = P(i - 1) + Pi
P(i-1) = 2Pin - Pi

Casi no se usa porque cuando se tienen varias fases no converge 
'''
from time import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from scipy.sparse.linalg import gmres
from scipy.sparse.linalg import bicgstab
import sympy as sy

Pin = 1500
Pout = 1000
#Para que la presión esté entre las presiones de frontera
Pinicial = (Pin + Pout) / 2
nx = 10
Lx = 1000

P_actual = np.zeros(nx)
P_anterior = np.ones(nx) * Pin 

deltat = 1

#Teimpo de simulación
tiempoTotal = 800
tiempo = 0

#Debe tener unidades para que sea consistente
c1 = 500

#Malla o divisiones del medio discreto. La malla tiene 5 centros y 6 divisiones 
gridx = np.linspace(0 , Lx , nx + 1)

#Distancia / longitud de la malla, es uniforme
deltax = Lx / nx

#Centros de la malla
gridc = np.linspace(deltax / 2 , Lx - deltax / 2 , nx)

while tiempo < tiempoTotal:

    #Condición de frontera izquierda oeste (W)
    P_actual[0] = ((((P_anterior[1] - 2 * P_anterior[0] + 2 * Pin - P_anterior[0]) / deltax ** 2)) * (deltat / c1)) + P_anterior[i]

    #Condición de frontera derecha este (E)
    P_actual[nx - 1] =((((2 * Pout - P_anterior[nx - 1] - 2 * P_anterior[nx - 1] / deltax ** 2)))) ((((P_anterior[1] - 2 * P_anterior[0] + 2 * Pin - P_anterior[0]) / deltax ** 2)) * (deltat / c1)) + P_anterior[i]


    #Se deben propagar las condiciones a la frontera porque se está resolviendo en los centros 
    for i in range(1 , nx - 1):
        
        P_actual[i] = ((((P_anterior[i + 1] - 2 * P_anterior[i] + P_anterior[i - 1]) / deltax ** 2)) * (deltat / c1)) + P_anterior[i]

    plt.title("Ecuación de difusión")
    plt.plot(gridc , P_actual)
    plt.xlabel('Distancia [ft]')
    plt.ylabel('Presión [PSI]')
    plt.show()
    P_vieja = np.copy(P_actual)

    print("Tiempo de sumulación: " , tiempo)
    tiempo = tiempo + deltat

#Cuando llega al estado estable no varía más