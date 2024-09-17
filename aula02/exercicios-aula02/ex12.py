categoria = input("Digite a categoria do empregado (A, B ou C): ").upper()
salario = float(input("Digite o salário atual do empregado: "))

percentualAumento = 0

if categoria == 'A':
    percentualAumento = 10
elif categoria == 'B':
    percentualAumento = 15
elif categoria == 'C':
    percentualAumento = 25
else:
    print("Categoria inválida! Por favor, insira A, B ou C.")

salarioComAumento = salario + (salario * percentualAumento / 100)

print(f"Salário atual: R${salario:.2f}")
print(f"Salário com aumento: R${salarioComAumento:.2f}")
