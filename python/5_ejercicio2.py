def conversor (segundos: int)->str:
     minutos = segundos // 60
     return "El valor ingresado en segundos es igual a {} minutos" .format(minutos)

print(conversor(240)) 
