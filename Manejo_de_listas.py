numeros = []
longitud = int(input("¿Cuantos numeros enteros contendra la lista?: "))

for _ in range(longitud):
    numeros.append(int(input("Introduce un numero entero: ")))

print(f"\nLista: {numeros} \nLa suma total de los elementos es: {sum(numeros)}")
