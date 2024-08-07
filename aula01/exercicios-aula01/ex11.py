nomeProd = input("Digite o nome do produto: ")
descProd = input("Digite a descrição do produto: ")
qtdComprada = int(input("Digite quantas unidades desse produto você comprou: "))
precoProd = float(input("Digite o preço desse produto: "))

total = qtdComprada * precoProd

print(f"Você comprou {qtdComprada} {nomeProd} com a descrição: {descProd}.")
print(f"E o preço total foi: {total}")