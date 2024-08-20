numero = int(input("1, 2, 3 - Categoria A \n 4, 5, 6 - Categoria B \n Escolha o número: "))

#Usando Case com mais de uma opção
match numero:
    case 1|2|3:
        print("Você escolheu a categoria A")
    case 4|5|6:
        print("Você escolheu a categoria B")
    case _: 
        print("Resposta inválida, escolha outro número.")