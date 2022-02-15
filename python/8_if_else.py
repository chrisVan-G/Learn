
'''
numero = int(input("Digite un número: ")) # Este es un programa para diferencar números positivos de negativos

if numero == 0:
    print ("El número es nulo")  # Es un problema de tres caminos por lo que uso if, elif, else

elif numero > 0:
    print ("El número es positivo")

else:
    print("El número es negativo")
'''

'''
nota = int(input("Digite la calificación: "))

if nota < 0 or nota > 50:
    print("Nota incorrecta")

elif nota >= 0 and nota < 30:
    print("Reprobado")

else:
    print("Aprobado")
'''

# Hacer un programa que me pida dos numeros y me diga cuál es par o si ambos son pares

'''
num1 = int(input("Digite numero1: "))
num2 = int(input("Digite numero2: "))

if(num1 %2 == 0 and num2 %2 == 0):
    print("Ambos números son pares")
    
elif(num1 %2 == 0 and num2 %2!= 0):
    print(f"{num1} es par")

elif(num1 %2!= 0 and num2 %2 == 0):
    print(f"{num2} es par")

else:
    print("Ambos numeros son impares")
'''

# Hacer un programa que pida tres números y determine cuál es el mayor

'''
num1 = int(input("Digite numero 1: "))
num2 = int(input("Digite numero 2: "))
num3 = int(input("Digite numero 3: "))

if (num1 > num2 and num1 > num3):
    print(f"{num1} es mayor")

elif (num2 > num1 and num2 > num3):
    print(f"{num2} es mayor")
    
else:
    print(f"{num3} es mayor")
'''

# Hacer un programa que pida un caracter e indique si es vocal o no

letra = input("Digite un caracter: ")

if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    print("Es una vocal")

else: 
    print("No es una vocal")
