equipamentos = []
valores = []
numerosSeriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    numerosSeriais.append(int(input("Número serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("\nDigite \"S\" para continuar: ").upper()

busca = input("Digite o nome do equipamento que deseja: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor.........: ", valores[indice])
        print("Número Serial.:", numerosSeriais[indice])
