nome1 = input("Digite seu nome: ")
nome2 = input("Digite seu nome: ")
peso1 = float(input("Digite o seu peso:"))
peso2 = float(input("Digite o seu peso:"))

if peso1 == peso2:
    print(f"As pessoas {nome1} e {nome2} tem pesos iguais")
elif peso1 > peso2:
    print(f"O usuário {nome1} é mais pesado que {nome2}")
elif peso2 > peso1:
    print(f"O usuário {nome2} é mais pesado que {nome1}")