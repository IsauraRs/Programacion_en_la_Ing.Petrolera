#Matemáticas simbólicas
import sympy as sy
#Importa infinito
from sympy import oo

#Convierte las etiquetas en símbolos
x = sy.Symbol('x')
y = sy.Symbol('y')

print(x + y + x - y)

#pprint escribe de forma más legible
sy.pprint(x ** 2 + 2 * y + 5 + x ** 2 + 3 * y + 10)  

#Para expandir las funciones algebráicamente
print(sy.expand((x + y) ** 7))

sy.pprint(sy.expand(x + y) ** 3)

#Para simplificar
sy.pprint(sy.simplify((x + x * y)) / x)

#Descomposición parcial de fracciones
sy.pprint(sy.apart(1 / ((x + 2) * (x + 1 + y)) , x))

#Limites
sy.pprint(sy.limit(sy.sin(x) / x , x , 0))
sy.pprint(sy.limit(1 / x , x, oo))

#Derivación
sy.pprint(sy.diff(sy.sin(x) , x))

#Derivada de orden 1
sy.pprint(sy.diff(sy.sin(2 * x) , x , 1))

#Derivada de orden 2
sy.pprint(sy.diff(sy.sin(2 * x) , x , 2))

#sy.pprint(sy.diff(sy.sin(x ** 5 + 2 * y , x , 1)))

#Expansión de series de Taylor (en este caso se indicó hasta el 10mo término)
sy.pprint(sy.cos(x).series(x , 0 , 10))

#Integrales indefinidas
sy.pprint(sy.integrate(6 * x ** 5 + sy.acot(x) , x))
sy.pprint(sy.integrate(x , x))
sy.pprint(sy.integrate(sy.sin(x) , x))

#Integrales definidas
sy.pprint(sy.integrate(x ** 2 , (x , 0 , 2)))