rows = int(input("¿Cuantas filas tendra la matriz?: "))
columns = int(input("¿Cuantas columnas tendra la matriz?: "))

matrix = []

for row_position in range(rows):
    row = []
    for element in range(columns):
        row.append(int(input(f"Introduce un elemento a la fila {row_position}: ")))
    matrix.append(row)

for row in matrix:
    print(row)
