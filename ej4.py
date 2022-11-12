#!/usr/bin/env python3
"""
Autor : 
Fecha   : 
Propósito: Calcular la soluicón de una ecuación de segundo grado
"""

print('Ecuación ax² + bx + c = 0')
a=int(input('Escribe el valor del coeficiente a: '))
b=int(input('Escribe el valor del coeficiente b: '))
c=int(input('Escribe el valor del coeficiente c: '))

discriminante = b**2 - 4*a*c  # lo de dentro de la raíz cuadrada

# Según la teoría matemática . . .
#Si a=0, la ecuación no tiene solución
#Si discriminante > 0, hay dos soluciones reales y distintas.
#Si discriminante = 0, tiene una solución.
#Si discriminante < 0, no tiene solución.

if a == 0:
    print('Sin solución')   
elif discriminante < 0 :
    print('Sin solución')
elif discriminante == 0 :
    print(f'Una solución {-b/(2*a)}')
else:
    x1 = (-b + (discriminante)**(1/2))/(2*a)
    x2 = (-b - (discriminante)**(1/2))/(2*a)
    print(f'Dos soluciones: {x1} {x2}')



