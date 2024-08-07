votosBrancos = int(input("Digite o número de votos brancos: "))
votosNulos = int(input("Digite o número de votos nulos: "))
votosValidos = int(input("Digite o número de votos válidos: "))

totalEleitores = votosBrancos + votosNulos + votosValidos

percBrancos = (votosBrancos * 100) / totalEleitores if totalEleitores > 0 else 0
percNulos = (votosNulos * 100) / totalEleitores if totalEleitores > 0 else 0
percValidos = (votosValidos * 100) / totalEleitores if totalEleitores > 0 else 0

print(f"O percentual de votos dessa eleição com o total de {totalEleitores} eleitores é:\n"
      f"Percentual de votos brancos: {percBrancos:.2f}%\n"
      f"Percentual de votos nulos: {percNulos:.2f}%\n"
      f"Percentual de votos válidos: {percValidos:.2f}%")
