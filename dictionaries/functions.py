def perguntar():
    resposta = input("O que deseja realizar? " + "I - para Inserir o usuário" + "P - para Pesquisar o usuário"
                     + "E - para Excluir o usuário" + " L - para Listar o usuário").upper()
    return resposta


def inserir(dicionario):
    chave = input("Digite o login: ").upper()
    dicionario[chave] = [input("Digite o nome: ").upper(),
                       input("Digite a última data de acesso: "),
                       input("Qual a última estação acessada? ").upper()]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista! = None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)! = None:
        del dicionario[chave]
    print("Objeto eliminado!")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)