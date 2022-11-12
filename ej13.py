#!/usr/bin/env python3
"""
Autor : 
Fecha   : 
Propósito: Calcular la letra del DNI
"""

dni = int(input("Dime tu DNI: "))
letras='TRWAGMYFPDXBNJZSQVHLCKE'
letraDNI = letras[dni%23]
print(f'Tu NIF es: {dni}{letraDNI}')