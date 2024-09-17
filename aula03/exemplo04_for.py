# Localizar valores em uma lista
localizar = "Laranja"
frutas = ["Maçã", "Banana", "Mamão", "Laranja", "Morango", "Uva", "Maracujá"]

for i in frutas:
    if i == localizar:
        print(f"Encontrou a fruta {localizar}")
        break
    else:
        print(f"{localizar}, Fruta não encontrada")
