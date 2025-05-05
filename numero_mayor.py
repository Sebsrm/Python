print("=======================================")
print("Programa para encontrar el número mayor")
print("======================================= \n")

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

if numero1 > numero2 and numero1 > numero3:
    print("El número mayor es:", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("El número mayor es:", numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("El número mayor es:", numero3)
else:
    print("Los números son iguales")

