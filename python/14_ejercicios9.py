'''# Realice un programa que compruebe si el año es bisiesto

def main(informacion:dict):
    
    p_fecha = informacion['fecha']
    
    if p_fecha != 0:
        if p_fecha %4 == 0:
            print("El año", p_fecha, "es bisiesto")
        else:
         print("El año", p_fecha, "no es bisiesto")
    else:
        print("Por favor ingrese un número diferente de cero")

informacion = {"fecha":2020}

print(main(informacion))
'''

'''nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
year = int(2021-edad)

dic = {1:nombre, 2:apellido, 3:year, 4:edad}

if (dic[4] <18):
    mayorEdad = int(year + 18)
    print("eres menor de edad, bla bla bla", mayorEdad)

elif(dic[4] > 18) and (dic[4] < 25):
    print("Tienes un 10% de descuento")

elif(dic[4] >25):
    print("Lo sentimos pero no tienes descuento")
    
elif (dic[4] == 18 and dic[4] == 25):
    print("premio, descuento es pecial del 20%")

print("Nombre completo: ", dic[1], dic[2])

if (year <=0):
    print("Año de nacimiento no puede calcularse")

else:
    print("Año de nacimiento: ", dic[3])'''

tp = int(input("Digite la temperatura: "))

dic = {1: tp}

if (dic[1] <= 10 and dic[1] >= -10 ):
    print("La temperatura es FRIA")

elif (dic[1] > 10 and dic[1] <= 20):
    print("La temperatura es NUBLADA") 

elif (dic[1] > 20 and dic[1] <= 30):
    print("La temperatura es CALUROSO") 
    
elif (dic[1] > 30 and dic[1] <= 50):
    print("La temperatura es TROPICAL")
else:
    print("La temperatura no esta en nuestra base de medición")
