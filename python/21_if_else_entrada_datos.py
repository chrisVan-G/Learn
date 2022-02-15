
# Condicionales con entrada de datos por teclado

num1 = int(input("Digite el número 1: "))
num2 = int(input("Digite el número 2: "))

operacion = input("Digite la operación: ") .upper()
if operacion == 'S':
    suma = num1 + num2
    print(f"La suma es {suma}")

elif operacion  == 'R':
    resta = num1 - num2
    print(f"La resta es {resta}")
    
elif operacion  == 'M':
    multiplicacion = num1 * num2
    print(f"La multiplicación es {multiplicacion}")

elif operacion  == 'D':
    division = num1 / num2
    print(f"La división es {division}")
else:
    print(f"Operación {operacion} no fue encontrada, por favor digite S, R, M ó D")
