print("Ejercicio #1:")

fruits = {"manzanas": 5,
          "peras": 2,
          "naranjas": 4
          }

print(fruits)

num_manzanas = fruits.get("manzanas")
print(f"Cantidad de manzanas con el metodo get(): {num_manzanas}")

num_manzanas = fruits["manzanas"]
print(f"Cantidad de manzanas consultando el valor: {num_manzanas}")
