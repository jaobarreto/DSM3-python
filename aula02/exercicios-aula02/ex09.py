print("Informe o de acordo com a lista o índice de poluição da sua área.")
indicePoluicao = int(input(" 0 - 2 Categoria 1 \n 3 - 5 Categoria 2 \n 6 - 7 Categoria 3 \n 8 - ... Categoria 4 \n Informe o número: "))

match indicePoluicao:
    case 0|1|2:
        print("Considerar aceitável")
    case 3|4|5:
        print("Suspender as atividades do Grupo 1")
    case 6|7:
        print("Suspender as atividades do Grupo 1 e 2")
    case 8:
        print("Suspender as atividades de todos os Grupos")
    case _:
        print("Indisponível.")