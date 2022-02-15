def triangulo (base: float, lado: float, altura: float):

 perimetro = base + lado + lado
 area = (base * altura)/2
 return "El perimetro del triangulo es de {} cm y el area es de {} cm "  .format(perimetro,area)

base = float(input("Introduce la base del triangulo:  "))
lado = float(input("Introduce el lado del triangulo:  "))
altura = float(input("Introduce la altura del triangulo:  "))

print(triangulo(base,lado,altura))
