rg = input("Digite o RG do empregado: ")
anoNascimento = int(input("Digite o ano de nascimento: "))
anoIngresso = int(input("Digite o ano de ingresso na empresa: "))
anoAtual = int(input("Digite o ano atual: "))

idade = anoAtual - anoNascimento
tempoTrabalho = anoAtual - anoIngresso

print(f"Idade do empregado: {idade} anos")
print(f"Tempo de trabalho: {tempoTrabalho} anos")

if idade >= 65:
    print("Requerer aposentadoria")
elif tempoTrabalho >= 30:
    print("Requerer aposentadoria")
elif idade >= 60 and tempoTrabalho >= 25:
    print("Requerer aposentadoria")
else:
    print("Não requerer Aposentadoria")