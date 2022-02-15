
# Determinar el perimetro y area de un triángulo 

def triangulo (base: float, lado: float, altura: float):

 perimetro = base + lado + lado
 area = (base * altura)/2
 return "El perimetro del triángulo es de {} cm y el área es de {} cm "  .format(perimetro, area)

base = float(input("Introduce la base del triángulo:  "))
lado = float(input("Introduce el lado del triángulo:  "))
altura = float(input("Introduce la altura del triángulo:  "))

print(triangulo(base, lado, altura))
