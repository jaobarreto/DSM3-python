print("Responda 1-sim 0-não \n Empréstimo")
negativo = int(input("Possui nome negativo? "))

if negativo == 1:
    print("Não pode realizar empréstimo")
else:
    carteiraAssinada = int(input("Possui carteira assinada? "))
    if carteiraAssinada == 0:
        print("Não pode realizar empréstimo")
    else:
        casaPropria = int(input("Possui casa própria? "))
        if casaPropria == 0:
            print("Não pode realizar empréstimo")
        else:
            print("Conceder empréstimo")