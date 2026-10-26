#Registro de incidencias
control = {}
for incidencia in range(1,6):
    while True:
        categoria = input(f"Ingrese la categoria {incidencia}: ").strip().upper()
        if categoria in ("RED","DATOS","APP"):
            break
        print("Categoria invalida")
    if categoria in control:
        control[categoria] += 1
    else:
        control[categoria] = 1
for categoria in control:
    print(f"{categoria}: {control[categoria]}")
    
print(f"Categoria diferentes: {len(control)}")