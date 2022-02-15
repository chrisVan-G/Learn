def muv (velocidad: float, tiempo: float)-> str:
     
 tiempoMinutos = tiempo * (1/60)

 distancia = velocidad * tiempoMinutos

 return "la distancia que la motocicleta ha recorrido es de: {} km" .format(distancia) 

print(muv(120,55))
