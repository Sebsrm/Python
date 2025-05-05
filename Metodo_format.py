#Metodo 1
nombre = input("¿Cual es tu nombre?: ")
edad = int(input("¿Cual es tu edad?: "))

print("Hola {} tienes {} años".format(nombre, edad)) 

#Metodo 2
print("Hola {nom} tienes {ed} años".format(nom = "Sebastian", ed = 18))

#Metodo 3
nom = "Sebastian"
ed = 18
print("Hola {1} tienes {0} años".format(ed, nom))