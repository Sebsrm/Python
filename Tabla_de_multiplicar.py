num = input("Ingrese un número para mostrar su tabla de multiplicar: ")

print(f"La tabla del {num} es:")
for i in range(21):
    print(f"{num} x {i} = {float(num) * i}")
