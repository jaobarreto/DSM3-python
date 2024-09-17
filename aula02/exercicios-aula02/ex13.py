pesoTerra = float(input("Digite o peso da pessoa na Terra (em kg): "))
numeroPlaneta = int(input("Digite o número do planeta (1 a 5): "))

gravidadeRelativa = 0

if numeroPlaneta == 1:
    gravidadeRelativa = 0.37
    planeta = "Mercúrio"
elif numeroPlaneta == 2:
    gravidadeRelativa = 0.88
    planeta = "Vênus"
elif numeroPlaneta == 3:
    gravidadeRelativa = 0.38
    planeta = "Marte"
elif numeroPlaneta == 4:
    gravidadeRelativa = 2.64
    planeta = "Júpiter"
elif numeroPlaneta == 5:
    gravidadeRelativa = 1.15
    planeta = "Saturno"
else:
    print("Número do planeta inválido! Por favor, insira um número entre 1 e 5.")
    exit()

pesoPlaneta = pesoTerra * gravidadeRelativa

print(f"Peso no planeta {planeta}: {pesoPlaneta:.2f} kg")
