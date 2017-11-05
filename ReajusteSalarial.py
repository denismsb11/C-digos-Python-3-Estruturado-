salario = float(input("Qual o salario do funcionario? R$"))
reajuste = 5
salario_com_reajuste = salario + (salario*reajuste/100)
print("Com um aumento de {}% o salário do funcionario passou a ser R${:.2f}"
      .format(reajuste,salario_com_reajuste))
