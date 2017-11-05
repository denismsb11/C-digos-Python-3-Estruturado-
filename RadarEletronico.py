velocidade = float(input("Qual a velocidade atual do carro em Km? "))
if velocidade >= 80:
    print("Voce foi multado! O limite de velocidade permitida é de 80Km/h")
    multa = (velocidade-80) * 6
    print("A multa será de R${:.2f}".format(multa))
    print("Digiraja com segurança!")
else:
    print("Parabéns, você está dirindo na velocidade adequada :D")
    print("Digiraja com segurança!")