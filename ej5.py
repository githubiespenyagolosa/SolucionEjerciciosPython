#!/usr/bin/env python3
"""
Autor : 
Fecha   : 
Propósito: Cálculo de áreas
"""

print('Cálculo de áreas - Elige una figura geomñetrica: ')
print('a) Triángulo')
print('b) Círculo')
figura=input('¿Qué figura quieres calcular (escribe T o C)? ').upper()
if figura=='T':
    base=float(input('Escribe la base: '))
    altura=float(input('Escribe la altura: '))
    area=base*altura/2
    print(f'Un triángulo de base {base} y altura {altura} tiene un área de {area}')
elif figura=='C':
    radio=float(input('Escribe el radio: '))
    area=3.14*radio**2
    print(f'Un círculo de radio {radio} tiene un área de {area}')
else:
    print('No es un círculo o un triángulo')