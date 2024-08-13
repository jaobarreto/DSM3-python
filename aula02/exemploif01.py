nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2
#estrutura condicional IF
if media > 6:
    print("Aluno aprovado!")
elif media >=2 and media < 6:
    print("Aluno Exame")
else:
    print("Aluno reprovado.")