
def termometro(nombre_temperatura: dict):
    
    d_nom = nombre_temperatura ['nombre']
    d_tem =  nombre_temperatura ['temperatura']
    
    if (d_tem < -10 or d_tem > 44):
        return 'Temperatura fuera de rango'
    else:
         if (d_tem >= -10 and d_tem <= 9):
             mensaje = 'hace mucho frio'
             
         elif (d_tem >= 10 and d_tem <= 14):
             mensaje = 'hace poco frio'
         
         elif (d_tem >= 15 and d_tem <= 24):
             mensaje = 'hace una temperatura normal'
         
         elif (d_tem >= 25 and d_tem <= 29):
             mensaje = 'hace poco calor'
         
         elif (d_tem >= 30 and d_tem <= 44):
             mensaje =  'hace mucho calor'
    return "Mi nombre es {} y la temperatura actual es de {} grados, {} ". format(d_nom, d_tem, mensaje)

nombre_temperatura = {
    'nombre': 'Juan David',
    'temperatura': 35
}
print(termometro(nombre_temperatura))
