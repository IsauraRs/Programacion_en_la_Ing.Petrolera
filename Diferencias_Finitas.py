'''Las diferencias finitas se obtienen de las series de Taylor
Para obtener la primer derivada se cortan los términos a partir del 3er grado y se despeja,
el término de segundo grado se cancela matemáticamente.
Para la discretización se utilizan las diferencias centrales.
'''
import matplotlib.pyplot as plt

x = sy.Symbol('x')
y = sy.Symbol('y')

f = sy.Function('f')
g = sy.Function('g')
f = x * 3.0
h = 1e-02

#Derivada algebráica
da = ((sy.diff(f , x).subs(x , 1).evalf()))
#Diferencia adelantada
diff_fo = (((f.subs(x , 1 + h).evalf()) - f.subs(x , 1).evalf())) / h
relative_error = (sy.Abs(da - diff_fo) / da) * 100
print("Error relativo mediante la diferencia adelantada: " , relative_error)

#Diferencia atrasada
dfb



n = 100
funcion = np.zeros(n)
der_alg = np.zeros(n)
der_num = np.zeros(n)
varInd = np.linspace(-10. , 10 , n)