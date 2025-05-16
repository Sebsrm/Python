#Diccionario vacio
dictionary_empty = {}

print(f"Diccionario vacio: {dictionary_empty}")
print()

#Diccionario homogeneo
dictionary_ages = {"Juan": 16, 
                   "Sebastian": 17, 
                   "Ramos": 18
                   }

print(f"Diccionario de edades: {dictionary_ages}")
print()

#Diccionario heterogeneo
dictionary_dates = {"name": "Hanna", 
                    "last_name": "Isabel",
                    "age": 17
                    }

print(f"Diccionario de edades: {dictionary_dates}")
print()

#Un diccionario puede almacenar listas y diccionarios
dictionary_list = {"a": {"a": 1},
                   "b": [0, 1, 2]
                   }

print(f"Diccionario con lista y diccionario: {dictionary_list}")
print()

#Un diccionario puede tener claves numericas 
dictionary_keys_num = {4: 1,
                       5: 2,
                       6: 3
                       }

print(f"Diccionario con claves numericas: {dictionary_keys_num}")
print()

#Un diccionario no puede tener claves repetidas
dictionary_repeated_keys = {"Juan": 20,
                            "Sebastian": 30,
                            "Juan": 15
                            }

print(f"Diccionario con claves repetidas: {dictionary_repeated_keys}")
print()

#Un diccionario puede tener claves numericas o de tipo texto
dictionary = {1: 23,
              "juan": 5,
              -2: "hola"
              }

print(f"Diccionario con claves de distintos tipos de dato: {dictionary}")
