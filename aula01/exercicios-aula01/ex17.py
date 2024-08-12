custoFabricacao = float(input("Digite o custo de fabricação desse carro: "))
percentualDistribuidor = 28/100
impostos = 45/100

valorDistribuidor = custoFabricacao * percentualDistribuidor
valorImpostos = custoFabricacao * impostos

carroNovo = custoFabricacao + valorDistribuidor + valorImpostos

print(f"O custo total desse carro novo é: {carroNovo:.2f} R$")
