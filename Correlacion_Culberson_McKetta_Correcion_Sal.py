from Correlacion_Culberson_McKetta import Rswp_Culberson_McKetta
import matplotlib.pyplot as plt
import numpy as np

#Correción para sal hasta 30,000 [ppm] 1% - 3%  70°F < T < 250°F
def Rsw_Culberson_McKetta(p, T, S):

    Rswp = Rswp_Culberson_McKetta(p , T)
    Rsw = 10 ** (-0.0840655 * S * T **-0.255854) * Rswp 
    print("Factor de corrección Rsw / Rswp = " , Rsw / Rswp)

    return Rsw

#La salinidad se ingresa en %, 20,000[ppm] = 2%
Rsw_ej = Rsw_Culberson_McKetta(5000 , 200 , 2)

print("Despejando Rsw = " , Rsw_ej)

#psi
presion = np.array([200 , 600 , 1000 , 1500 , 2000 , 3000 , 4000 , 5000 , 7000 , 10000])

#°F
temperatura = np.linspace(80 ,340 , 20 )


for i in range(0 , len(presion)):

    Rswp = Rswp_Culberson_McKetta(presion[i] , temperatura)
    Rsw = Rsw_Culberson_McKetta(presion[i] , temperatura , 2)
    plt.figure("Rswp vs Rsw" , figsize = (6 , 8))
    plt.plot(temperatura, Rswp , '-b')
    plt.plot(temperatura, Rsw , '-k')

plt.title("Rswp vs Rsw")
plt.xlabel("Temperatura[°F]")
plt.ylabel("Presión[psi]")
plt.grid()
plt.show()
plt.savefig("RswpvsRsw.png" , dpi = 300)

#El agua salada no permite disolver tanto gas