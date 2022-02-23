
# set/conjuntos van entre {}

'''
conjunto = set()
conjunto = {1,2,2,3,344, 'Hola', 1.5}
conjunto.add('Juan') # para agregar elementos
conjunto.add(7)
print(conjunto)
'''

'''
a = {1,2,3}
b = {3,2,1}
print(a == b)
'''

a = {1,2,3}
b = {3,2,1,4} 
c = a | b # Se unifican los dos conjuntos
print(c)
