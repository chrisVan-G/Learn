def cargarSocios(numero: int, nombre: str, fecha: str, cuota: str):
    usuario_activos[numero]=[nombre, fecha, cuota]
    print("Ingreso con exito")
    return usuario_activos

def numeroSocio(socios, nombre):
    for numero, datos in socios.items():
        if datos[0].lower()==nombre.lower():
            return numero
    return 0

def formatoFecha(fecha):
    return (fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:])

def imprimirListado(socios):
    for numero, datos in socios.items():
        print("Número:", numero)
        print("Nombre:", datos[0])
        print("Ingresó:", formatoFecha(str(datos[1])))
        print("Estado:", datos[2])
        print("--------------------------")

usuario_activos={1:["Juan David Triana", 20042015, "Cuota al día"], 2:["Daniel Acosta", 20022015, "Cuota al día"], 3:["Rafael Maya", 30052016, "Cuota al día"]}

print ("---------------------------------") 
print("Ingresar usuario al GYM")

numero = int(input("Digite el número del usuario: "))
nombre = str(input("Digite el nombre del usuario: "))
ingreso = str(input("Digite la fecha de ingreso del usuario: "))
cuota = str(input("Digite el pago de cuota del usuario: "))
usuario_activos = cargarSocios(numero, nombre, ingreso, cuota)
print ("---------------------------------")

print("Registrar pago de cuotas")
usuarioPagoCuota = int(input("Digite el número del usuario a modificar: "))
usuario_activos[usuarioPagoCuota][2]= str(input("Registre el pago de cuotas: "))
print("Actualizacion de pago de cuotas exitoso")
print ("---------------------------------") 

print("Eliminar usuario") 
usuarioEliminado = int(input("Ingrese el número del usuario a eliminar: "))
nombre = usuario_activos[usuarioEliminado][0]
usuarioEliminado = numeroSocio(usuario_activos, nombre)
if usuarioEliminado in usuario_activos :
    del usuario_activos[usuarioEliminado]
    print("Usuario ",nombre,", eliminado exitosamente") 
        
else:
    print ("El usuario no se encuentra registrado")
print ("---------------------------------")

print("Imprimir los socios activos") 
print("---------------------------------") 

imprimirListado(usuario_activos)