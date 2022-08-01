def preencherInventario(lista):
    resposta = "S"
    while resposta == "S":
        equipamento = [input("Equipamento: "),
                       float(input("Valor: ")),
                       int(input("Número Serial: ")),
                       input("Departamento: ")]
        lista.append(equipamento)
        resposta = input("Digite \"S\" para continuar: ").upper()


def exibirInventario(lista):
    for elemento in lista:
        print("\nNome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Número Serial: ", elemento[2])
        print("Departamento.: ", elemento[3])


def localizarPorNome(lista):
    busca = input("\nDigite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor........: ", elemento[1])
            print("Número Serial: ", elemento[2])
            print("Departamento.: ", elemento[3])


def depreciarPorNome(lista, porc):
    depreciacao = input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print("Novo valor: ", elemento[1])


def excluirPorSerial(lista):
    serial = int(input("\nDigite o número serial que deseja excluir: "))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return "Itens excluídos!"


def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: R$", max(valores))
        print("O equipamento mais barato custa: R$", min(valores))
        print("O valor total em equipamento é de: R$", sum(valores))