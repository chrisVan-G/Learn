
# Ciclos for

'''
for variable in secuencia:
    instrucciones
'''

'''
for letra in "Colombia":
    print(letra)
else:
    print("\n")
    print("Fin del ciclo")
'''

'''
for letra in "Christian":
    if letra == "i":
        print(letra)
'''

'''
for letra in "Colombia":
    if letra == "o":
        print(letra)
        break
        #continue
'''

# Hacer un programa que al ingresar un número me muestre las tablas de multiplicar

'''
operacion = int(input("Digite la tabla que necesita procesar: "))

for n in range(1,11):
    resultado = operacion * n
    print (f"{operacion} X {n} = {resultado}")
'''

# Este es mi programa

'''
mult = int(input('Digite la tabla que desea conocer: '))
print(f'{mult} X 1 = {mult}')
n = 1
while n >= 1 and n <= 10:
    n = n + 1 
    resultado = mult * n
    print(f'{mult} X {n} = {resultado}')
    if n == 10:
        break
'''

'''
from ctypes.wintypes import HACCEL


for i in [1,2,3,4]:
    print("Hola")
    
print("--------------------------------------")

for i in [1,2,3,4]:
    print(i)

print("--------------------------------------")

for i in ["otono", "primavera", "invierno", "verano"]:
    print(i)

print("--------------------------------------")

for i in ["otono", "primavera", "invierno", "verano"]:
    print("Hola")

print("--------------------------------------")

for letra in "Colombia":
    print("Hola")

'''

# Si range recibe 1 parámetro (7) imprime los datos hasta el punto establecido -1 (0,1,2,3,4,5,6)
# Si range recibe 2 parámetros (1, 7) inicia el el parámetro 1 y fanaliza en el punto establecido -1 (1,2,3,4,5,6)
# Si range recibe 3 parámetros (1, 11, 2) inicia el el parámetro 1 y fanaliza en el punto establecido -1 aumentando 
# según el tercer valor (1,3,5,7,9)

for i in range(8):
    print(i)
