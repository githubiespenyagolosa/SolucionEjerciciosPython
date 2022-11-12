#!/usr/bin/env python3
"""
Autor : 
Fecha   : 
Propósito: Lista de todos los divisores de un número introducido
"""

'''
Los divisores de un número natural son los números naturales que lo pueden dividir, 
resultando de cociente otro número natural y de resto 0. 
'''

numero= int(input('Dime un número: '))
lista_divisores=[]
cantidad = 0
	
for i in range(1, numero+1): 
	if numero%i == 0:
		lista_divisores.append(i)
		cantidad += 1
	
	
print (f'{numero} tiene {cantidad} divisores: {lista_divisores}')

