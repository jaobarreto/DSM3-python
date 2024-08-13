altura1 = float(input("Digite uma altura: "))
altura2 = float(input("Digite outra altura: "))
altura3 = float(input("Digite outra altura: "))

alturas = [altura1, altura2, altura3]
#sort é um método que lista em ordem crescente
alturas.sort()

print(f"A ordem crescente é {alturas[0]}, {alturas[1]} e {alturas[2]}")

#se não quiser usar o sort faça assim:
altura1 = float(input("Digite uma altura: "))
altura2 = float(input("Digite outra altura: "))
altura3 = float(input("Digite outra altura: "))

if altura1 <= altura2 and altura1 <= altura3:
    menor = altura1
    if altura2 <= altura3:
        medio = altura2
        maior = altura3
    else:
        medio = altura3
        maior = altura2
elif altura2 <= altura1 and altura2 <= altura3:
    menor = altura2
    if altura1 <= altura3:
        medio = altura1
        maior = altura3
    else:
        medio = altura3
        maior = altura1
else:
    menor = altura3
    if altura1 <= altura2:
        medio = altura1
        maior = altura2
    else:
        medio = altura2
        maior = altura1

print(f"A ordem crescente é {menor}, {medio} e {maior}")

