def fatorial(n):
    if(n == 1):
        return 1
    else:
        n * fatorial(n-1)

def main():
    n = int(input("Digite um n qualquer: "))
    fat = fatorial(n)
    print("{}".format(fat))

if(__name__ == "__main__"):
    fatorial()