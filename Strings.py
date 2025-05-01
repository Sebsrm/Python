mensaje = "Hola"
mensaje += " "
mensaje += "Sebastian"
print (mensaje)

print("concatenación:")

mensaje = "Hola"
espacio = " "
nombre = "Sebastian"
print(mensaje + espacio + nombre)

numero_uno = 2
numero_dos = 4
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado de la suma es: " + resultado)

print("Busqueda:")

mensaje = "Hola Sebastian"
buscar_subcadena = mensaje.find("Sebastian")
print(buscar_subcadena)

print("Extracción:")

mensaje = "Hola Sebastian"
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)

print("Comparación:")

mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)
