#!/usr/bin/env python3
"""
Autor : 
Fecha   : 
Propósito: Escribir mayor, menor y media
"""

valores=int(input('¿Cuántos valores vas a introducir?: '))
media, suma, maximo = 0, 0, 0
minimo=1000000000000000000000

for i in range(1,valores+1):
    numero=int(input(f'Dime el número {i}: '))
    suma+=numero
    if numero<minimo:
        minimo=numero
    elif numero>maximo:
        maximo=numero

media = suma/valores

print(f'El número más pequeño de los introducidos es: {minimo}')
print(f'El número más grande de los introducidos es: {maximo}')
print(f'La media de los números introducidos es: {media}')