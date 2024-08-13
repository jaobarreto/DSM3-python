print("Responda 1-Masculino 0-Feminino \nSexo")
sexo = int(input("Qual seu sexo? "))

if sexo == 1 or sexo == 0:
    altura = float(input("Digite a sua altura (em metros): "))
    if sexo == 1:
        pesoIdeal = 72.7 * altura - 58
        print(f"Seu peso ideal é: {pesoIdeal:.2f} kg")
    elif sexo == 0:
        pesoIdeal = 62.1 * altura - 44.7
        print(f"Seu peso ideal é: {pesoIdeal:.2f} kg")
else:
    print("Sexo inválido. Por favor, responda 1 para Masculino ou 0 para Feminino.")
