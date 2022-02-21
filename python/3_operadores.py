
# Operadores

'''
Expresión de calculos

Operadores y expresiones
simbolos(operadores) y calculos(expresiones)

operadores sobre int y float = [+, -, *, /, inverso aditivo(-), exponenciación(**), división entera(//), módulo(%)]

Operadores de comparación 
Se aplican a int y float y entregan un resultado de tipo bool < <= > >= != ==

Operadores lógicos
Se aplican a datos de tipo bool y entregan un tipo bool not and or 

Operadores para datos tipo str concatenación(+) y repetición(*)
'''

# Manipulando datos. Conversiones de tipos

# Conversiones a str
# print("Son las " + (3+6)) # genera error
print("Son las " + str(3+6)) # error solucionado al convertir valores enteros a str

# Conversiones a int
print("El valor entero es", int(3.5565))
print("El resultado de la suma es", int("3") + 12)
print("El resultado de la suma es", float("3.6") + 12)

# Para operar entre valores, estos deben tener el mismo tipo de dato



'''
x = int(input("Digite un número al azar:  "))
y = 10

suma = x + y
print("La suma es:  ", suma)
resta = x - y
print("La resta es:  ", resta)
multi = x * y
print("La multiplicación es:  ", multi)
div = x / y
print("La división es:  ", div)
pot = x ** y
print("La potencia es:  ", pot)
divEnteros = x // y
print("La divEnteros es:  ", divEnteros)
modulo = x % y
print("El modulo es:  ", modulo)
'''

var1 = 10
var2 = 4
var3 = 5.5
var4 = 67

promedio = (var1 + var2 + var3 + var4) / 4

print("El promedio de esos numeros es ", float(promedio))
