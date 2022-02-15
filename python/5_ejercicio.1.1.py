def  conversor(pies: int, pulgadas: float)->str:
     cm = pies * 30.48
     cm += pulgadas * 2.54
     
     return "La conversión en centimetros es: {} cm" .format(cm);
     
pies = int(input("Ingrese el valor para pies: "))
pulgadas = float(input("Ingrese en valor para pulgadas"))

print(conversor(pies,pulgadas))
