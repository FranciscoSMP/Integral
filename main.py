from sympy import *
import os
f = input('\n\tIngrese la funcion definida: ')
x = symbols('x')
x0 = input('\tIngrese el limite inferior: ')
x1 = input('\tIngrese el limite superior: ')
res2 = integrate(f,(x,x0,x1))
print(f'\n\n\tEl resultado es {res2}\n\n')
os.system("pause")