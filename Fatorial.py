n = int(input("Digite um valor qualquer: "))
fat = 1
for x in range(1,n+1):
    fat *= x
print("O faltorial de {}! é {}".format(n,fat))