first_name = input("Por favor introduce tu nombre: ")
last_name = input("Por favor introduce tu apellido: ")
full_name = f"{first_name} {last_name}"

print()
print(f"¿El formato del metodo title se ha aplicado?: {full_name.istitle()}")
print(f"Aplicando el metodo title(): {full_name.title()}")
print(f"Volvemos a imprimir el nombre: {full_name}")

print()
full_name = full_name.title()
print(f"¿El formato del metodo title se ha aplicado?: {full_name.istitle()}")
print(f"Se ha aplicado el metodo title de manera permanente: {full_name}")
