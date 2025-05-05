print("========================================================")
print("* Programa para determinar si un número es par o impar *")
print("======================================================== \n")

numero = float(input("Por favor introduce un número entero: "))

if numero % 2 == 0:
    print("El número", numero, " es par.")
elif numero % 2 == 1:
    print("El número", numero, " es impar.")
else:
    print("El número", numero, " no es un número entero.")


