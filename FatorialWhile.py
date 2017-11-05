n = int(input("Digite um valor qualquer: "))
fat = 1
i = 1
while(n >= i):
    fat *= i
    i = i+1
print("O fatorial de {}! é {}".format(n,fat))