print("***************************************")
print("* Sistema de control vacacional Rappi *")
print("*************************************** \n")

nombre_empleado = input("por favor introduce el nombre del empleado: ")
clave_departamento = int(input("Por favor introduce la clave del departamento: "))
antiguedad = int(input("Por favor introduce los años laborados del empleado: "))

#Sentencias condicionales multiples
if clave_departamento == 1:

    if antiguedad == 1 and antiguedad < 2:
        print("El empleado ", nombre_empleado, " tiene derecho a 6 dias de vacaciones.")
    elif antiguedad >= 2 and antiguedad <= 6:
        print("El empleado ", nombre_empleado, " tiene derecho a 14 dias de vacaciones.")
    elif antiguedad >=7:
        print("El empleado ", nombre_empleado, " tiene derecho a 20 dias de vacaciones.")
    else:
        print("El empleado ", nombre_empleado, " aún no tiene derecho a vacaciones.")
 
elif clave_departamento == 2:

    if antiguedad == 1 and antiguedad < 2:
        print("El empleado ", nombre_empleado, " tiene derecho a 7 dias de vacaciones.")
    elif antiguedad >= 2 and antiguedad <= 6:
        print("El empleado ", nombre_empleado, " tiene derecho a 15 dias de vacaciones.")
    elif antiguedad >=7:
        print("El empleado ", nombre_empleado, " tiene derecho a 22 dias de vacaciones.")
    else:
        print("El empleado ", nombre_empleado, " aún no tiene derecho a vacaciones.")

elif clave_departamento == 3:

    if antiguedad == 1 and antiguedad < 2:
        print("El empleado ", nombre_empleado, " tiene derecho a 10 dias de vacaciones.")
    elif antiguedad >= 2 and antiguedad <= 6:
        print("El empleado ", nombre_empleado, " tiene derecho a 20 dias de vacaciones.")
    elif antiguedad >=7:
        print("El empleado ", nombre_empleado, " tiene derecho a 30 dias de vacaciones.")
    else:
        print("El empleado ", nombre_empleado, " aún no tiene derecho a vacaciones.")
        
else:
    print("La clave del departamento no existe, vuelve a intenntarlo.")
