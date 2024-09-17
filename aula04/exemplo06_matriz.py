linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

matrizNumeros = []

for i in range(linhas):
    linha = []
    matrizNumeros.append(linha)
    for j in range(colunas):
        numero = float(input(f"Digite o número da posição({i,j})"))
        linha.append(numero)
for i in matrizNumeros:
    print(i)
