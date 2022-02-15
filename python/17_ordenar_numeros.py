
# Pedir tres números y mostrar ordenados de mayor a menor

def numeros(informacion:dict):
    
    a = informacion['numero1']
    b = informacion['numero2']
    c = informacion['numero3']
        
    if (a > b and b > c):
         print('a', a, 'b', b, 'c', c)
         
    elif (a > c and c > b):    
         print('a', a, 'c', c, 'b', b)
         
    elif (b > a and a > c):    
         print('b', b, 'a', a, 'c', c)
         
    elif (b > c and c > a):
          print('b', b, 'c', c, 'a', a)
         
    elif (c > b and b > a):
         print('c', c, 'b', b, 'a', a)
         
    elif (c > a and a > b):
         print('c', c, 'a', a, 'b', b)
         
    informacion = {'numero1' : 1,'numero2' : 2,'numero3': 3}  
        
    print(numeros(informacion))
