'''
Un método implícito implica que se toma en n + 1 (el tiempo actual)

C * (Pi ^ (n+1) - Pi ^ n) / deltat = (P( i + 1) - 2Pi + P(i -1) / deltax ^ 2)^ ( n + n)
Pi ^ ( n + 1) * (C / deltat + 2 / deltax^2) ) = 1 / deltax^2 P (i + 1) ^ ( n + 1) + (1 / deltax^2) P(i - 1) ^ (n + 1) + CPi^n / deltat
'''

from time import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from scipy.sparse.linalg import gmres
from scipy.sparse.linalg import bicgstab
import sympy as sy

aP = np.zeros(nx) * 2.0
aE = np.zeros(nx)
aW = np.zeros(nx)
B = np.zeros(nx)

Pin = 1500
Pout = 1000
#Para que la presión esté entre las presiones de frontera
Pinicial = (Pin + Pout) / 2
nx = 10
Lx = 1000

P_actual = np.zeros(nx)
P_anterior = np.ones(nx) * Pin 

#Matriz de coeficientes
A = np.zeros((nx , nx))

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

    #Se deben propagar las condiciones a la frontera porque se está resolviendo en los centros 
    for i in range(0 , nx):

        aP[i] = c1 / deltat + 2 / deltax ** 2
        aE[i] = 1 / deltax ** 2
        aW[i] = 1 / deltax ** 2
        B[i] = (c1 / deltat) * P_anterior[i]

    #Condición a la frontera izquierda
    aP[0] = aP[0] + aW[0]
    B[0] = aW[0] * 2 * Pin

    #Condición a la frontera de primera clase derecha (E) Pout
    aP[nx-1] = aP[nx - 1]  + aE[nx - 1]
    B[nx - 1] = B[nx - 1] * 2 * Pout

    #LLenado de la matriz de coeficientes 
    for i in range( 0 ,nx) : 

        A[i][i] = aP[i]

    for i in range(0 , nx - 1):

        A[i][i + 1] = -aE[i]

    for i in range(1 , nx):

        A[i][i - 1] = -aW[i]

    #Se transforma a una matriz tipo lista de scipy
    A1 = lil_matrix(A)

    #Formaato de filas comprimidas
    A1 = A1.tocsr()

    #Resuelve el álgebra lineal correspondiente
    Press01 = spsolve(A1 , B)



    plt.title("Ecuación de difusión")
    plt.plot(gridc , P_actual)
    plt.xlabel('Distancia [ft]')
    plt.ylabel('Presión [PSI]')
    plt.show()
    
    P_vieja = np.copy(P_actual)

    print("Tiempo de sumulación: " , tiempo)
    tiempo = tiempo + deltat
