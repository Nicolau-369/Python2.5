nome = input("Qual o seu nome? ")
try:
    if nome == "Nicolau":
        raise NameError("Não gosto desse nome")
    print("Olá, %s" % nome)
except NameError:
    print("O programa não gosta desse nome")