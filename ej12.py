#!/usr/bin/env python3
"""
Autor : 
Fecha   : 
Propósito: Dibujar un rectángulo
"""

anchura=int(input('Anchura del rectángulo: '))
altura=int(input('Altura del rectángulo: '))

for i in range(1,altura+1):
    for j in range(1, anchura+1):
        print('*', end=" ")
    print()