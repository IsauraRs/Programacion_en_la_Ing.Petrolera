#Factor de compresibilidad del gas, p.22
#from matplotlib.lines import _LineStyle
import numpy as np
import matplotlib.pyplot as plt

A1 = 0.3265
A2 = -1.07
A3 = -0.5339
A4 = 0.01569
A5 = -0.05165
A6 = 0.5475
A7 = -0.7361
A8 = 0.1844
A9 = 0.1056
A10 = 0.6134
A11 = 0.721


def z_Dranchuk_Kassem(Psr, Tsr, z_guess):
    
    error = 10
    iteracion = 0

    while error > 1E-07:

        Rhor = 0.27 * Psr / (z_guess * Tsr)

        F = z_guess - (1 + (A1 + A2 / Tsr + A3 / Tsr ** 3 + A4 / Tsr ** 4 + A5 / Tsr ** 5) * Rhor)
        + ((A6 + A7 / Tsr + A8 / Tsr **2 ) * Rhor ** 2) - ((A9 * (A7 / Tsr + A8 / Tsr ** 2)) * Rhor ** 5)
        + A10 * (1 + A11 * Rhor ** 2) * (Rhor ** 2 / Tsr ** 3) * np.exp(-A8 * Rhor ** 2)

        dF_dz = 1 + ((A1 + A2 / Tsr + A3 / Tsr ** 3 + A4 / Tsr ** 4 + A5 / Tsr ** 5) * Rhor / z_guess)
        + 2 * ((A6 + A7 / Tsr + A8 / Tsr ** 2) * Rhor ** 2 / z_guess) - 5 * A9 * ((A7 / Tsr + A8 / Tsr ** 2) * (Rhor ** 5 / z_guess))
        + ((2 * A10 * Rhor ** 2) / (z_guess * Tsr ** 3)) * (1 + A11 * Rhor ** 2 - (A11 * Rhor ** 2) ** 2) * np.exp(-A11 * Rhor ** 2)

        z_next_guess = z_guess - F / dF_dz

        error = abs(z_next_guess - z_guess)

        print("Error = " , error)

        z_guess = z_next_guess
        
        iteracion += 1
        print(iteracion)

    return float(z_guess)


Psr = np.linspace(1 , 14 , 30)
Tsr = np.linspace(1.2 , 3 , 15)
zf = np.zeros(len(Psr))

plt.figure("Z_factor")

for i in range(0 , len(Tsr)):
    for j in range(0, len(Psr)):

        zf[j] = z_Dranchuk_Kassem(Psr[j] , Tsr[i] , 0.7)

    plt.plot(Psr , zf , 'k--')

plt.title('z Dranchuk-Kassem')
plt.xlabel('Presión Pseudoreducida (Psr)')
plt.ylabel('Factor de compresibilidad (z)')

plt.minorticks_on()
plt.grid(True , which = 'major' , color = 'k' , linestyle = '-')
plt.grid(b = True , which = 'minor' , color ='g' , linestyle = '--')
plt.show()
plt.savefig('z-Dranchuk-Kassem.png' , dpi = 1200)
