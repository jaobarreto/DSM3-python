num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

if num1 <= 0 or num2 <= 0:
    print("Os números devem ser positivos!")
else:
    print("\n Escolha uma opção:")
    print("1. Média ponderada, com pesos 2 e 3, respectivamente")
    print("2. Quadrado da soma dos 2 números")
    print("3. Cubo do menor número")

    escolha = int(input("Digite o número da opção: "))

    if escolha == 1:
        mediaPonderada = (num1 * 2 + num2 * 3) / (2 + 3)
        print(f"A média ponderada é: {mediaPonderada:.2f}")
    elif escolha == 2:
        soma = num1 + num2
        quadradoSoma = soma ** 2
        print(f"O quadrado da soma dos dois números é: {quadradoSoma:.2f}")
    elif escolha == 3:
        menorNumero = min(num1, num2)
        cuboMenor = menorNumero ** 3
        print(f"O cubo do menor número é: {cuboMenor:.2f}")
    else:
        print("Opção inválida")