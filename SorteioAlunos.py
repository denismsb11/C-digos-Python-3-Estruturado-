import random
aluno1 = str(input("Digite o nome do aluno(a): "))
aluno2 = str(input("Digite o nome do aluno(a): "))
aluno3 = str(input("Digite o nome do aluno(a): "))
aluno4 = str(input("Digite o nome do aluno(a): "))
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(lista) # Retorna um dos itens da lista
print("O aluno escolhido foi: {}".format(escolhido))