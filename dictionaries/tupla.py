ips = {}
resposta = "S"
while resposta == "S":
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois últimos octetos: "))] = input("Nome da máquina: ")
    resposta = input("Digite \"S\" para continuar").upper()
print("Exibindo IP's: ")
for ip in ips.keys():
    print(ip[0] + "." + ip[1])
print("Exibindo máquinas com o mesmo endereço...")
pesquisa = input("Digite os dois últimos octetos: ")
for ip, nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes)")
    if ip[1] == pesquisa:
        print(nome)
print("Exibindo máquinas quem compõem a mesma rede...")
rede = input("Digite os dois primeiros octetos: ")
for ip, nome in ips.items():
    if ip[0] == rede:
        print(nome)
