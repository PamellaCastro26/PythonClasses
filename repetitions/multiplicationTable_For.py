tabuada = int(input("Digite o número da tabuada: "))
print("Tabuada do número ", tabuada)
for valor in range(0, 11, 1):
    print(str(tabuada) + "x" + str(valor) + " = " + str((tabuada*valor)))
