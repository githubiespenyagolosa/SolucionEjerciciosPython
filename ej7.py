#!/usr/bin/env python3
"""
Autor : 
Fecha   : 
Propósito: Escribir una lista de números
"""

numero=int(input('Dime un número: '))
if numero >= 0:
    for i in range(0,numero-1):
        if i==0:
            print(start='[',i,end=', ')
        else:
            print(i,end=', ')
    print(numero,end=']')
else:
    for i in range(0,numero,-1):
        if i==0:
            print(start='[',i,end=', ')
        else:
            print(i,end=', ')
    print(numero)