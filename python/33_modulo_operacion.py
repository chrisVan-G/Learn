
from modulos import modulos as operacion

print()

a = int(input("Ingrese un valor para 'a' por favor: "))
b = int(input("Ingrese un valor para 'b' por favor: "))

print("-----------------------------------------------")

resultado = operacion.sumar(a, b)
print("El resultado de la suma es:", resultado)

resultado = operacion.restar(a, b)
print("El resultado de la resta es:", resultado)

resultado = operacion.mult(a, b)
print("El resultado de la multiplicación es:", resultado)

resultado = operacion.division(a, b)
print("El resultado de la división es:", resultado)

print("-----------------------------------------------")
