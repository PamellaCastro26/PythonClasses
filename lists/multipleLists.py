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
    resposta = input("Digite \"S\" para continuar: ").upper()
for equipamento in equipamentos:
    print("Equipamento: ", equipamento)
