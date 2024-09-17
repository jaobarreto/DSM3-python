# Exemplo vetor para definir o tamanho do vetor
tamanho = int(input("Digite o tamanho do vetor: "))
vetor = []

for i in range(tamanho):
    elemento = int(input(f"Digite o elemento {i +1}°: "))
    vetor.append(elemento)
print(f"Vetor {vetor}")
