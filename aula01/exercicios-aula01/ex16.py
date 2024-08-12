nome = input("Digite o seu nome: ")
anoNascimento = int(input("Digite em qual ano você nasceu: "))
idade = abs(anoNascimento - 2024) #abs torna o valor absoluto, assim fazendo com que ele seja positivo e não negativo

print(f"Olá {nome} você tem {idade} anos.")