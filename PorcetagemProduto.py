produto = float(input("Digite o preço do produto: R$"))
desconto = 5
produto_com_desconto = produto - (produto * 0.005)
print("O produto recebendo um desconto de {}% irá custar R${:.2f}"
      .format(desconto,produto_com_desconto))