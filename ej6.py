#!/usr/bin/env python3
"""
Autor : 
Fecha   : 
Propósito: Distancia en km, m y cm
"""

print('Distancia en km, m y cm')
distancia_inicial=int(input('Introduce una distancia en cm: '))
# Determina si hay algún kilómetro dividiendo entre 100000
distancia_km = distancia_inicial // 100000
# Determina si hay algún metro dividiendo el resto de la operación anterior entre 100
distancia_m = (distancia_inicial % 100000) // 100
# Determina si hay algún centímetro calculando el resto de la distancia inicial entre 100
distancia_cm = distancia_inicial % 100

if distancia_inicial > 0:
        if distancia_km > 0:
                if distancia_m > 0:
                        print(f'{distancia_inicial} centímetros son {distancia_km} kms, {distancia_m} m y {distancia_cm} cm')
        elif distancia_m > 0:
                print(f'{distancia_inicial} centímetros son {distancia_m} m y {distancia_cm} cm')
        elif distancia_cm > 0:
                print(f'{distancia_inicial} centímetros son {distancia_cm} cm')
else:
        print('Introduce un número mayor que cero')



