#!/usr/bin/env python3
"""
Autor : 
Fecha   : 
Propósito: Distancia en km, m y cm
"""

print('Distancia en km, m y cm')
distancia_inicial=int(input('Introduce una distancia en cm: '))
# Determina si hay algún Km dividiendo entre 100000
distancia_km = distancia_inicial // 100000
# Determina si hay algún m dividiendo el resto de la operación anterior entre 100
distancia_m = (distancia_inicial % 100000) // 100
# Determina si hay algún cm calculando el resto de la distancia inicial entre 100
distancia_cm = distancia_inicial % 100

if distancia_inicial > 0:
    frase_final = f'{distancia_inicial} centímetros son'
    if distancia_km > 0:
        frase_final += f' {distancia_km} kms'
    if distancia_m > 0:
        frase_final += f', {distancia_m} m'
    if distancia_cm > 0:
        frase_final += f', {distancia_cm} cm'
    print(frase_final+'.')
else:
        print('Introduce un número mayor que cero')


