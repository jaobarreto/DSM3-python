from math import pi
raio = float(input("Digite o valor do raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))

volume = pi * pow(raio,2) * altura

print(f"O volume desse cilindro é: {volume}")