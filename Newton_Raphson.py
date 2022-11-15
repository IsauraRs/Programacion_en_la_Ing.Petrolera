import sympy as sy
from sympy import oo

def Newton_Raphson(function, guess):

    error = 10.0
    iteracion = 0
    epsilon = 1E-05
    
    while (error > epsilon):
        next_guess = guess - (function.subs(x , guess).evalf() / sy.diff(function , x).subs(x , guess).evalf())
        error = abs(next_guess - guess) / next_guess * 100
        guess = next_guess
        iteracion += 1
        print("Valor de la raíz: ", guess , "Error relativo: " , error , "Iteraciones: " , iteracion)

x = sy.Symbol('x')
f = sy.Function('f')

f = -120 - 46 * x + 79 * x ** 2 - 3 * x ** 3 - 7 * x ** 4 + x ** 5

raiz = Newton_Raphson(f,10)
print(raiz)