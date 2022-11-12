#!/usr/bin/env python3
"""
Autor : 
Fecha   : 
Propósito: Suma de cifras
"""

print('Suma de las cifras de un número')
numero=input('Dime un número: ')
suma = 0

for num in numero:
    suma += int(num)

print(f'La suma de las cifras del número {numero} es {suma}.')