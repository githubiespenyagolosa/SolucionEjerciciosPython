#!/usr/bin/env python3
"""
Autor : 
Fecha   : 
Propósito: Crear una lista de palabras
"""

numero_palabras=int(input('Dime cuántas palabras tiene la lista: '))

lista_palabras = []

for i in range(1, numero_palabras+1):
    lista_palabras.append(input(f'Introduce la palabra {i}: '))

print(f'La lista creada es: {lista_palabras}')
lista_palabras.reverse()
print(f'La lista inversa es: {lista_palabras}')
