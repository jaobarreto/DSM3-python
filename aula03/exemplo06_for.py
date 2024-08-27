# Armazenar valores em uma lista utilizando for
listaNumeros = []

for i in range(1,6):
    numero = int(input(f"Digite o {i}° número: "))
    listaNumeros.append(numero)

print("Números armazenados: ")
for i in listaNumeros:
    print(i)