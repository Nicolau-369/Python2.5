class usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def diga_ola(self):
        print("Olá, meu nome é %s e meu email é %s" % (self.nome, self.email))

usuario1 = usuario(nome="Nicolau", email="Niccolo369@proton.me")

usuario1.diga_ola()
print(usuario1.nome)

usuario1.nome = "Nicolau Yasuke"
print(usuario1.nome)

print(hasattr(usuario1, "nome"))
print(hasattr(usuario1, "idade"))
print(getattr(usuario1, "email"))
setattr(usuario1, "nome", "Nicolau Y.")
setattr(usuario1, "idade", 42)
print(getattr(usuario1, "nome"))
print(getattr(usuario1, "idade"))
delattr(usuario1, "idade")
print(getattr(usuario1, "idade"))