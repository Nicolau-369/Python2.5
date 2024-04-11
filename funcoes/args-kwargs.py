def print_tudo_2_vezes(*args):
    for parametro in args:
        print(parametro + "! " + parametro + "!")

print_tudo_2_vezes("Olá", "Python", "Nicolau")

def print_info(**kwargs):
    for parametro, valor in kwargs.items():
        print(parametro + " - " + str(valor))

print_info(nome="Nicolau", idade =42, nacionalidade="Latveriano")

def print_info(nome, idade, **kwargs):
    print("Nome: " + nome)
    print("Idade: " + str(idade))

    print("\nInformações adicionais:")
    for parametro, valor in kwargs.items():
        print(parametro + " - " + str(valor))

print_info(nome="Nicolau", idade=42, nacionalidade="Latveriano", Email="Niccolo369@proton.me")