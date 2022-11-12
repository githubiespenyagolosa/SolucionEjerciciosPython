#!/usr/bin/env python3
"""
Autor : 
Fecha   : 
Propósito: Cambiar las vocales de una frase por una vocal que introduce el usuario
"""

frase_original = input('Dime algo: ')
vocal = input('Dime una vocal: ')
frase_resultado = frase_original

for i in 'aeiouAEIOU':
  frase_resultado = frase_resultado.replace(i, vocal)

print(f'La frase es ahora: {frase_resultado}')