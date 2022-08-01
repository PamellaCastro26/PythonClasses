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

serial = int(input("Digite o número serial do equipamento que será excluído: "))
for indice in range(0, len(equipamentos)):
    if numerosSeriais[indice] == serial:
        del equipamentos[indice]
        del valores[indice]
        del numerosSeriais[indice]
        del departamentos[indice]
        break

for indice in range(0, len(equipamentos)):
    print("\nEquipamento...: ", (indice+1))
    print("Nome..........: ", equipamentos[indice])
    print("Valor.........: ", valores[indice])
    print("Número serial.: ", numerosSeriais[indice])
    print("Departamento..: ", departamentos[indice])
