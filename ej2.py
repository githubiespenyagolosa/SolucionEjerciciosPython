#!/usr/bin/env python3
"""
Autor : 
Fecha   : 
Propósito: Conversión de segundos a minutos
"""

print('Convertidor de segundos a minutos')
segundos=int(input('Escribe una cantidad de segundos: '))
minutos=segundos//60
segundos2=segundos%60
print(f'{segundos} segundos son {minutos} minutos y {segundos2} segundos')