import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

datos = pd.read_excel('datos.xlsx')
press = np.array(datos['Presión [psia]'])[::]
BgV = np.array(datos['Bg [RB/scf]'])[::]
MugV = np.array(datos['Mug [cp]'])[::]

plt.figure("Datos Leídos")
plt.plot(press , BgV , '-.bs')
plt.xlim((np.min(press) , np.max(press)))
plt.ylim((np.min(BgV) , np.max(BgV)))
plt.xlabel('Presión [psi]')
plt.ylabel('Factor de volumen del gas (Bg)')
plt.grid()
plt.title('P vs Bg')

plt.show()

plt.figure("Datos μg ")
plt.plot(press , MugV , '--go')
plt.xlim((np.min(press) , np.max(press)))
plt.ylim((np.min(MugV) , np.max(MugV)))
plt.xlabel("Presión [psi]")
plt.ylabel("Viscosidad del gas (μg)")
plt.grid()
plt.title('P vs μg')

plt.show()