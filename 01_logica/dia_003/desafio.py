# Sistema de tarifas de estacionamiento

numero_horas = int(input("Ingrese el numero de horas de estacionamiento: "))
total = 0

if 1 <= numero_horas <= 2:
    total += 5
    print(f"S/{total}")
elif 3 <= numero_horas <= 5:
    total += 10
    print(f"S/{total}")
elif 6 <= numero_horas <= 10:
    total += 20
    print(f"S/{total}")
elif numero_horas > 10:
    total += 30
    print(f"S/{total}")
elif numero_horas <= 0:
    print("Error")

