#range(inicio,fim,salto) - Gera uma lista contendo uma progressão aritmética
# Os saltos desta função são opicionais, Se passamos só um paramêtro ele indica
#  o inicio = 0 e o salto = 1
#range(11) -> valores de 0 a 10
#range(11,41) -> valores de 11 a 40
#range(11,41,5) -> valores de 11 a 40, saltando de 5 em 5
# O in sempre irá ler uma lista, dessa forma o range sempre retorna uma lista

for w in range(2,100,10):
    print(w)
