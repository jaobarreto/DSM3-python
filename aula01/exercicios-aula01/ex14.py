valor = float(input("Digite o valor da parcela: "))
taxaJuros = float(input("Digite o valor da taxa de juros em porcentagem: "))
tempo = int(input("Digite quantos meses está atrasado: "))

valorAtraso = valor + (valor* (taxaJuros/100)*tempo)

print(f"O valor da prestação somada ao valor {valor}, foi {valorAtraso}")