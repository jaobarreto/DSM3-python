num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num2 == 0:
    print("Não é possível dividir por zero.")
elif num1 != num2:
    divisao = num1 / num2
    print(f"O resultado da divisão é {divisao}")
else:
    print("Os números são iguais. Divisão não realizada.")
