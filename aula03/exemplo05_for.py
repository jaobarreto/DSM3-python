# Mostrar os umeros de uma lista que são impares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numeros:
    if i % 2 == 0:
        continue
    print(f"Número ímpar: {i}")
