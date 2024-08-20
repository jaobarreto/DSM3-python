cat = input("Digite 'A' para calcular 10% \n Digite 'B' para calcular 15% \n Escolha uma letra: ")
valor = float(input("Digite o valor: "))

match (cat.lower()): #muda p letra miniscula e .upper() para letras maiusculas
    case "a":
        nv = (valor * 10)/100
        print(f"O cálculo de 10% é {nv:.2f}")
    case "b":
        nv = (valor * 15)/100
        print(f"O cálculo de 15% é {nv:.2f}")
    case _:
        print("Resposta inválidada, digite outra letra.")
        exit