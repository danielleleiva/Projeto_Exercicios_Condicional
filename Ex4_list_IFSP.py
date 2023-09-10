total_macas = int(input("Quantas maçãs você irá comprar?\n"))

if total_macas >= 12:
    custo1 = total_macas * 0.25
    print(f"Você comprou {total_macas} maçãs, o valor total da compra foi de: R${custo1:.2f}")
else:
    custo2 = total_macas * 0.30
    print(f"Você comprou {total_macas} maçãs, o valor total da compra foi de: R${custo2:.2f}")