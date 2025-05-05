print("Calculadora con una sola variable \n")

print("====================")
print("* Menú de opciones *")
print("==================== \n")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Modulo \n")

numero = float(input("Introduce un número: "))

if numero == 1:

    print("Has elegido la suma. \n")
    numero = float(input("Por favor introduce el primer numero: "))
    numero += float(input("Por favor introduce el segundo numero: "))
    print("El resultado de la suma es: ", numero)

elif numero == 2:

    print("Has elegido la resta. \n")
    numero = float(input("Por favor introduce el primer numero: "))
    numero -= float(input("Por favor introduce el segundo numero: "))
    print("El resultado de la resta es: ", numero)

elif numero == 3:

    print("Has elegido la multiplicación. \n")
    numero = float(input("Por favor introduce el primer numero: "))
    numero *= float(input("Por favor introduce el segundo numero: "))
    print("El resultado de la multiplicación es: ", numero)

elif numero == 4:

    print("Has elegido la división. \n")
    numero = float(input("Por favor introduce el primer numero: "))
    numero /= float(input("Por favor introduce el segundo numero: "))
    print("El resultado de la división es: ", numero)

elif numero == 5:

    print("Has elegido la división entera. \n")
    numero = float(input("Por favor introduce el primer numero: "))
    numero //= float(input("Por favor introduce el segundo numero: "))
    print("El resultado de la división entera es: ", numero)

elif numero == 6:

    print("Has elegido el exponente. \n")
    numero = float(input("Por favor introduce el primer numero: "))
    numero **= float(input("Por favor introduce el segundo numero: "))
    print("El resultado del exponente es: ", numero)

elif numero == 7:

    print("Has elegido el modulo. \n")
    numero = float(input("Por favor introduce el primer numero: "))
    numero %= float(input("Por favor introduce el segundo numero: "))
    print("El resultado del modulo es: ", numero)

else:
    print("La opción elegida no es válida, vuelve a intentarlo.")

