print("Ejercicio #2:")

fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }

print(fruits)

fruits["bananos"] = 5
print(f"Valor asignado: {fruits}")

fruits.setdefault("mangos", 6)
print(f"Metodo setdefault(): {fruits}")

fruits.update({"uvas": 3})
print(f"Metodo update(): {fruits}")
