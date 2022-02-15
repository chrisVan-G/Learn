
# Condicionales anidados

edad = int(input("Digita la edad: "))

if edad > 0 and edad < 102:
    print("Edad correcta")
    if edad >= 18:
        print("La persona es mayor de edad")
    else:
        print("La persona es menor de edad")

else:
    print("Edad incorrecta")
