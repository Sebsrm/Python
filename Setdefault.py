fruits = {"manzana": 2,
          "banano": 3,
          "naranja": 1
          }

print(f"{fruits} \n")

#Intentar agregar una clave que ya existe en el diccionario
return_value = fruits.setdefault("banano", 4)
print(f"El valor retornado de ('banano', 4) es: {return_value}")
print(f"El diccionario actualizado es: {fruits} \n")


#Intentaremos agregar una clave que no existe en el diccionario sin valor
return_value = fruits.setdefault("kiwi")
print(f"El valor retornado de ('kiwi) es: {return_value}" )
print(f"El diccionario actualizado es: {fruits} \n")


#Intentamos agregar una clave que no existe en el diccionario con valor
return_value = fruits.setdefault("mango", 5)
print(f"El valor retornado de ('mango', 5) es: {return_value}")
print(f"El diccionario actualizado es: {fruits} \n")
