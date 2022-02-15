
# Bucles o ciclos While

# Hace uso de iteradores (i)

'''
i = 0
while i <= 10:
    print(i)
    i += 1
else:
    print("Fin del ciclo")
'''

# while con funciones

'''
def main():
    print("Diga si, para terminar el programa")
    respuesta = input("Desea terminar con el programa: ")
    
    while respuesta != "si":
        respuesta = input("Desea terminar con el programa: ")
        
    print ("Fin del programa")

if __name__ == "__main__":
 main()
'''

'''
def main():
    print("Confirme su contraseña")
    print("------------------------------------")
    password_1 = input("Escriba su contraseña: ")
    password_2 = input("Escriba de nuevo su contraseña: ")
    
    while password_1 != password_2:
        print("las contraseñas son diferetes.¡Intentalo de nuevo!")
        password_1 = input("Escriba su contraseña: ")
        password_2 = input("Escriba de nuevo su contraseña: ")

    print("Contraseña confirmada")    
        
if __name__ == "__main__":
    main()
'''

'''
def main():
    print("Alcancía digital")
    print("------------------------------------")
    objetivo = float(input("Cuánto dinero en pesos desea ahorrar: "))
        
    ahorrado = 0.0;
        
    while objetivo > ahorrado:
            ahorrado += float(input("Cuántos pesos desea consignar a la alcancía "))
    
    sobrante = ahorrado - objetivo;
    
    print(f"Has cumplido tu objetivo, ahorraste ${ahorrado} dolares y tu sobrante es de ${sobrante} dolares.")
    
if __name__ == "__main__":
    main()

# revisar y optimizar, que si me paso de la meta me devuelva el excedente
'''

'''
numero = int(input("Digite un número: "))
while numero > 0:
    print("Actual valor del número: ", numero)
    numero = numero -1
    if numero == 5:
        break

'''

numero = int(input("Digite un número: "))
while numero > 0:
    print("Actual valor del número ", numero)
    numero = numero - 1
    if numero == 5:
     continue
