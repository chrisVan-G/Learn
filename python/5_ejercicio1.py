def  conversor(pies: int, pulgadas: float)->str:
     cm = pies * 30.48
     cm += pulgadas * 2.54
     
     return "La conversión en centimetros es: {} cm" .format(cm);

print(conversor(10, 5))
