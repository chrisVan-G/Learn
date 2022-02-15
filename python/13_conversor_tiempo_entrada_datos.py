
# Conversor de tiempo con entrada de datos

def conversor (segundos: int)->str:
     minutos = segundos // 60
     return "El valor ingresado en segundos es igual a {} minutos" .format(minutos)

segundos = int(input ("Ingrese la cantidad a convertir: "))

print(conversor(segundos))
