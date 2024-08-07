alturaParede = float(input("Digite a altura da parede: "))
larguraParede = float(input("Digite a largura da parede: "))
alturaAzulejo = float(input("Digite a altura do azulejo: "))
larguraAzulejo = float(input("Digite a largura do azulejo: "))
# tudo em metros
areaParede = alturaParede * larguraParede
areaAzulejo = alturaAzulejo * larguraAzulejo

totalAzulejos = areaParede / areaAzulejo

print(f"A parede com area total de: {areaParede}m² e os azulejos: {areaAzulejo}m²")
print(f"O total de azulejos para usar nessa parede foram: {totalAzulejos}")