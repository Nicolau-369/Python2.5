while True:
    nome = input("Digite seu nome ou sair para terminar o programa: ")
    if nome == "sair":
        break
    else:
        print("Olá, %s" % nome)