#!/usr/bin/env python3
"""
Autor : 
Fecha   : 
Propósito: Calculador de los años pasados
"""

año_actual=int(input('¿En qué año estamos?: '))
año_cualquiera=int(input('Escribe un año cualquiera: '))
if año_cualquiera>año_actual:
 años_restantes=año_cualquiera-año_actual
 print(f'Para llegar al año {año_cualquiera} faltan {años_restantes} años.')
if año_cualquiera<año_actual:
 años_pasados=año_actual-año_cualquiera
 print(f'Desde el año {año_cualquiera} han pasado {años_pasados} años.')
if año_cualquiera==año_actual:
 print('¡Son el mismo año!')