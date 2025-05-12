string = input("Introduce un string para invertirlo: ")
string_invertido = ""

for character in string:
    string_invertido = character + string_invertido

print(f"String invertido: {string_invertido}")
