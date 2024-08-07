salario = float(input("Digite o seu salário mensal: "))
reajuste = float(input("Digite a porcentagem do reajuste: "))

salarioAjustado = salario + (salario * (reajuste / 100))

print(f"O valor do seu salário {salario} obteve um reajuste de {reajuste}% e seu novo salário agora é: {salarioAjustado}")