import math
angulo = float(input("Digite o angulo que você deseja "))
seno = math.sin(math.radians(angulo))
print("O angulo {} possui o SENO = {:.2f}".format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print("O angulo {} possui o COSSENO = {:.2f}".format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print("O angulo {} possui a TANGENTE = {:.2f}".format(angulo,tangente))