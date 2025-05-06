free_fire = input("Introduce un string: ")

print(f"\n¿Todas las letras estan en minusculas?: {free_fire.isupper()}")
free_fire = free_fire.lower()
print(f"string en minusculas:  {free_fire}")

print(f"\n¿Todas las letras estan en mayusculas?: {free_fire.islower()}")
free_fire = free_fire.upper()
print(f"string en mayusculas:  {free_fire}")
