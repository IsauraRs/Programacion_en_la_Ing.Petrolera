'''
La solubilidad del gas metano en agua pura(no salina), Rswp, está en función de la presión 
y la temperatura.
Rswp = A + Bp + Cp^2
p[psi]
T[F]
'''
import numpy as np
import matplotlib.pyplot as plt 

#Se define la función

def Rswp_Culberson_McKetta(p, T):

    A = 8.15839 - 6.12265e-02 * T + 1.91663e-04 * T **2 - 2.1654e-07 * T **3
    B = 1.01021e-02 - 7.44241e-05 * T + 3.05553e-07 * T ** 2 - 2.94883e-10 * T ** 3
    C = (-9.02505 + 0.130237 * T - 8.53425e-04 * T ** 2 + 2.34122e-06 * T ** 3 - 2.37049e-09 * T ** 4) * 1e-07 

    Rswp = A + B * p + C * p ** 2
    
    return Rswp


#Con datos de un ejercicio 
Rswp_ej = Rswp_Culberson_McKetta(5000 , 200)
print("Rswp = " + str(Rswp_ej) + " [PCN / BN]")

#psi
presion = np.array([200 , 600 , 1000 , 1500 , 2000 , 3000 , 4000 , 5000 , 7000 , 10000])

#°F
temperatura = np.linspace(80 ,340 , 20 )

'''
Rswp = Rswp_Culberson_McKetta(presion[0] , temperatura)
#print("Rswp = " + str(Rswp_ej) + " [PCN / BN]")
plt.plot(temperatura , Rswp)
plt.grid()
plt.show()
'''
for i in range(0 , len(presion)):

    Rswp = Rswp_Culberson_McKetta(presion[i] , temperatura)
    plt.figure("Rswp" , figsize = (6 , 8))
    plt.plot(temperatura, Rswp)

plt.title("Rswp")
plt.xlabel("Temperatura[°F]")
plt.ylabel("Presión[psi]")
plt.grid()
plt.show()
plt.savefig("Rswp_Culberson_McKetta.png" , dpi = 300)

