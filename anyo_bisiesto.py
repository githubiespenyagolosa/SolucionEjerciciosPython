

anyo=int(input('Introduce un año para comprobar si es bisiesto: '))
condicion1=(anyo%4==0) and not (anyo%100==0)
condicion2=anyo%400==0
if condicion1 or condicion2:
    print(f'{anyo} es un año bisiesto.')
else:
    print(f'{anyo} no es un año bisiesto.')