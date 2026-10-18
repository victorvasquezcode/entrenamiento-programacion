# Control de acceso a una sala de servidores.

edad = int(input("Edad: "))
cuenta_activa = input("Cuenta Activa ? ")
suspendido = input("Suspendido ? ")
autorizacion_especial = input("Autorizacion especial ? ")
administrador = input("Administrador ? ")

# Reglas de acceso
esta_suspendido = suspendido == "si"

grupo_a = (
    edad >= 18 
    and cuenta_activa == "si" 
    and not esta_suspendido
)

grupo_b = (
    autorizacion_especial == "si" 
    or administrador == "si"
)

if grupo_a and grupo_b:
    print("Permitido")
else:
    print("Denegado")