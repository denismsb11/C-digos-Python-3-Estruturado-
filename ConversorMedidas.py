medida = float(input("Digite uma distância em metros: "))
dm = medida * 10
cm = medida * 100
mm = medida * 1000

dam = medida / 10
hm = medida / 100
km = medida / 1000
print("A medida de {}m corresponde a: ".format(medida))
print("{} dm \n{} cm \n{} mm".format(dm,cm,mm))
print("{} dam \n{} hm \n{} km".format(dam,hm,km))
#Perceba que \n pula uma linha na função print