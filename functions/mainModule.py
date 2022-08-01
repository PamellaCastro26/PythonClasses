from functions.functionIDs import *
minhaLista = []
print("Preenchendo...")
preencherInventario(minhaLista)
print("Exibir")
exibirInventario(minhaLista)

print("Pesquisando...")
localizarPorNome(minhaLista)
print("Alterando...")
depreciarPorNome(minhaLista, 20)

print("Excluindo...")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("Resumindo...")
resumirValores(minhaLista)
