'''
Ecuación de difusión en su forma más sencilla d2P / dx2 = 0 con condiciones de frontera de primera clase
Mediante el uso de diferencias finitas centrales y una discretización por celda o bloques centrados
Es un sistema tridiagonal, lo que cambia son los coeficientes 
La metodología de bloques centrados es la más usada
d2P / dx2 = (P(i + 1) - 2Pi + P(i-1)) / delta ** 2 = 0
Despejando para Pi (Presión donde estamos parados):
2Pi = P(i + 1) + P(i - 1)
ae = east, aw = west
apPi = aeP(i+1) + awP(i-1) + B
Para el nodo 0:
Pin = (P0 + P-1) / 2
P-1 = 2Pin - P0
aP = aeP1 + aw(2Pin - P0) + B0
(ap + aw)P0 = aeP1 + aw2Pin
Para el nodo 4:
(ap + ae)P4 = awP3 + ae2Pout

Las ecuaciones gobernantes en petróleo no tienen solución analítica
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from scipy.sparse.linalg import gmres
from scipy.sparse.linalg import bicgstab
import sympy as sy

#Número de nodos
nx = 5

#Longitud del medio
Lx = 1000

#Presión de entrada
Pin = 500

#Presión de salida
Pout = 1000

#Malla o divisiones del medio discreto. La malla tiene 5 centros y 6 divisiones 
gridx = np.linspace(0 , Lx , nx + 1)

#Distancia / longitud de la malla, es uniforme
deltax = Lx / nx

#Centros de la malla
gridc = np.linspace(deltax / 2 , Lx - deltax / 2 , nx)

#Coeficientes discretos de la ecuación general discreta, obtenidos de sustituir
#las diferencias finitas
aP = np.ones(nx) * 2.0
aE = np.ones(nx)
aW = np.ones(nx)
B = np.zeros(nx)

#Condición a la Frontera de primera clase (presión dada) izquierda (W) Pin
aP[0] = aP[0] + aW[0]
B[0] = aW[0] * 2 * Pin

#Condición a la frontera de primera clase derecha (E) Pout
aP[nx-1] = aP[nx - 1]  + aE[nx - 1]
B[nx - 1] = aE[nx - 1] * 2 * Pout

#Matriz de coeficientes
A = np.zeros((nx , nx))

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

x = sy.Symbol('x')

p = sy.Function('p')

#Representación de la ecuación 
edp = sy.Eq(p(x).diff(x , x) , 0)

#Solución matemática
psol = sy.dsolve(edp)
print(psol)

'''
Aplicando condiciones de frontera:
P(x) = C1 + C2X
P(0) = Pin
P(x) = Pin + C2X
P(x) = Pout
Pout = Pin + C2Lx
P(x) = Pin + (Pout - Pin)X / Lx
'''

sol_analitica = Pin  + (Pout - Pin) / Lx * gridc

plt.plot(gridc , Press01 , 'r')
plt.plot(gridc , sol_analitica, 'b--')
plt.xlabel('Distancia [ft]')
plt.ylabel('Presión [PSI]')
plt.show()