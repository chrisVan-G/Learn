
# Formula para hallar la velocidad

def vel (tiempo: int, distancia: int)-> str:
     velocidad = distancia / tiempo
     
     return "La velocidad es de {} metros/segundo" .format(velocidad) 
 
tiempo = int(input("Digite el tiempo: "))
distancia = int(input("Digite la distancia: "))

print(vel(tiempo, distancia))
