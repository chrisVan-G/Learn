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

#for formato in fecha.items(): 
#return formato[:2]+"/"+formato[2:4]+"/"+formato[4:]

def imprimirListado(socios):
    for numero, datos in socios.items():
        print("El número es: ", numero)
        print("El usuario: ", datos[0], "ingreso el: ", datos[1], "su estado es: ", datos[2])
        print("--------------------------")

usuario_activos={1:["Juan David Triana", 20042015, "cuota al día"], 2:["Daniel Acosta", 20022015, "cuota al día"], 3:["Rafael Maya", 30052016, "cuota al día"]}

print ("---------------------------------") 
print("Ingresar usuario al GYM")

numeroUsuario = int(input("Digite el ID del usuario: "))
nombreUsuario = str(input("Digite el nombre del usuario: "))
fechaIngresoUsuario = str(input("Digite la fecha de ingreso del usuario: "))
cuotaUsuario = str(input("Digite el estado del usuario: "))
usuario_activos=cargarSocios(numeroUsuario, nombreUsuario, fechaIngresoUsuario, cuotaUsuario)
print ("---------------------------------")

print("Registrar pago de cuotas")
usuarioPagoCuota = int(input("Digite el ID del socio a modificar: "))
usuario_activos[usuarioPagoCuota][2]= str(input("Digite el estado del usuario: "))
print("Actualizacion de pago de cuotas exitoso")
print ("---------------------------------") 

print("Eliminar usuario") 
usuarioEliminado = int (input ("Ingrese id del usuario a eliminar: "))
nombreSocio = usuario_activos[usuarioEliminado][0]
usuarioEliminado = numeroSocio(usuario_activos, nombreSocio)
if usuarioEliminado in usuario_activos :
    del usuario_activos[usuarioEliminado]
    print("Usuario ",nombreSocio,", eliminado exitosamente") 
else:
    print ("El usuario no se encuentra registrado")
print ("---------------------------------")

print("Imprimir los socios activos") 
print ("---------------------------------") 

#imprimirListado()
print(imprimirListado(usuario_activos))
