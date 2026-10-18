# Sistema de becas

promedio = float(input("Promedio: "))
asistencia = int(input("Porcentaje asistencia: "))
primer_puesto = input("Tiene primer puesto?: ")

if promedio >= 16 and asistencia >= 80 or primer_puesto == "si":
    print("Aprobado")
else:
    print("Desaprobado")