#Usando for com listas pré-definidas
lista = ["João", "Kamille", "Ravi", "Wagner", "Klaus"]

for i in lista:
    if len(i) !=4:
        continue
    print(f'Esses são os nomes com 4 letras: {i}')
    
    if i == "João":
        break
    print('Tchau')