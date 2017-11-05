from random import randint
from time import sleep
computador = randint(0,5)
print("==**=="*10)
print("Vou pensar em um numero entre 0 e 10. Tente adivinhar =D ")
print("==**=="*10)
chute = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(2)
if chute == computador:
    print("Parabéns, você acertou!")
    print("Estava pensando no número {}!".format(computador))
else:
    print("Infelizmente não foi dessa vez. Eu pensei no número {}".format(computador))