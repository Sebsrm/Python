invitados = ["Sebastian", "Sergio", "Jhon"]
amigos = ["Luis", "Juan"]
print(f"Lista invitados: {invitados} \nLista amigos: {amigos}")
invitados.extend(amigos)
print(f"Lista invitados: {invitados}")

numeros = [10, 20]
print(f"\nLista numeros: {numeros}")
numeros.extend(range(30, 100, 10))
print(f"Lista numeros: {numeros}")
