
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

mult = int(input('Digite la tabla que desea conocer: '))
print(f'{mult} X 1 = {mult}')
n = 1
while n >= 1 and n <= 10:
    n = n + 1 
    resultado = mult * n
    print(f'{mult} X {n} = {resultado}')
    if n == 10:
        break
