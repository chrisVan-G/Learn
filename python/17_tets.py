usuario_activos={1:["Juan David Triana","20042015","cuotaAlDia"], 2:["Daniel Acosta","25022015","cuotaAlDia"], 3:["Rafael Maya","30052016","cuotaAlDia"]}

print ("---------------------------------")
print("Ingresar usuario al GYM")
usuario_activos=cargarSocios(4,"Diana Marcela","01122016","cuotaEnMora")
print ("---------------------------------")

print("Registrar pago de cuotas")
usuarioPagoCuota=4
usuario_activos[usuarioPagoCuota][2]="cuotaAlDia"
print("Actualizacion de pago de cuotas exitoso")
print ("---------------------------------")

print("Eliminar usuario")
nombre= "Juan David Triana"
usuarioEliminado=usuarioEliminadoSocio(usuario_activos, nombre)
if usuarioEliminado in usuario_activos:
   del usuario_activos[usuarioEliminado]
print("Usuario ",nombre , ", eliminado exitosamente")
print ("---------------------------------")

print("Imprimir los socios activos")
print ("---------------------------------")
imprimirListado(usuario_activos)