totalCompra = float(input("Informe o total da compra: "))
formaPagamento = int(input("1 - À vista \n2 - Cartão de Débito \n3 - Cartão de Crédito \nEscolha a forma de pagamento: "))

match formaPagamento:
    case 1:
        print("Selecionado À vista, desconto de 15% aplicado")
        compraDesconto = totalCompra - (totalCompra * 0.15)
        print(f"O valor final da compra foi: R$ {compraDesconto:.2f}")
    case 2:
        print("Selecionado Cartão de Débito, desconto de 10% aplicado")
        compraDesconto = totalCompra - (totalCompra * 0.10)
        print(f"O valor final da compra foi: R$ {compraDesconto:.2f}")
    case 3:
        print("Selecionado Cartão de Crédito, desconto de 5% aplicado")
        compraDesconto = totalCompra - (totalCompra * 0.05)
        print(f"O valor final da compra foi: R$ {compraDesconto:.2f}")
    case _:
        print("Não identificado.")
