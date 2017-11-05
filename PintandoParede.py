altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))
base = altura*largura
print("Sua parede tem dimensão de {} x {} \nSua área é de {}m² ".format(altura,largura,base))
tinta = base/2 #Supondo que a cada 2m² você precisa de 1L de tinta para pintar
print("Para pintar a parede precisamos de {} L de tinta".format(tinta))
