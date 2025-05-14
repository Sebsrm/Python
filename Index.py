vocales = ["a", "e", "i", "o", "u", "a"]

print(f"Lista: {vocales}")
print(f"La letra a esta en la posicion: {vocales.index("a")}")
print(f"La letra i esta en la posicion: {vocales.index("i")}")
print(f"La letra u en el rango 2-final esta en la posicion: {vocales.index("u", 2)}")
print(f"La letra i en el rango 2-4 esta en la posicion: {vocales.index("i", 2, 4)}")

print(f"La letra u en el ranfo 2-4 esta en la posicion: {vocales.index("u", 2, 4)}")
#Esto lanzara un error porque no existe la letra u en el rango 2-4
