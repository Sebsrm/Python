print("Ejercicio #3")

fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }

print(fruits)

del fruits["peras"]
print(f"Funcion del: {fruits}")

fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }
print(fruits)

fruits.pop("peras")
print(f"Metodo pop(): {fruits}")
