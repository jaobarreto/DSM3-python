num1 = int(input("Digite um número inteiro: "))

if num1 % 2 == 0:
    resultado = num1 **2
    print(f"Ele é par e o quadrado dele é {resultado}")
else:
    resultado = num1 **3
    print(f"Ele é ímpar e o cubo dele é {resultado}")
    
