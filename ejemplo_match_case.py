# Ejemplo uso de match-case

# Pedimos el primer número
numero1=int(input('Introduce el primer número: '))
# Pedimos el segundo número
numero2=int(input('Introduce el segundo número: '))

# Pedimos la operación a realizar
operacion=input('Introduce la operación a realizar (+, -, *, /): ')

match operacion:
    case '+':
        resultado=numero1+numero2
    case '-':
        resultado=numero1-numero2
    case '*':
        resultado=numero1*numero2
    case '/':
        resultado=numero1/numero2
    case _:
        print('Opción no válida.')

print(f'El resultado es: {resultado}.')