print("**************** Cálculo de Grandesas Elétricas ****************")
grandezasEletricas = int(input(" 1. Tensão (em Volt) -------------- U = R * i \n 2. Resistência (em Ohm) -------------- R = U / i \n 3. Corrente (em Ampére) -------------- i= U / R \n Escolha uma para calcular: "))
print(f"{'*' * 20}")

match grandezasEletricas:
    case 1:
       R = float(input("Digite a Resistência:  "))
       i = float(input("Digite a Corrente: "))
       U = R * i
       print(f"A tensão em volts é {U}")
    case 2:
        U = float(input("Digite a Tensão: "))
        i = float(input("Digite a Corrente: "))
        R = U / i
        print(f"A Resistência é: {R}")
    case 3:
        U = float(input("Digite a Tensão: "))
        R = float(input("Digite a Resistência: "))
        i = U / R
        print(f"A Corrente é {i}")
    case _:
        print("Resposta inválida.")
        