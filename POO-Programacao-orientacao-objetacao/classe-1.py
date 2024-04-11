class Usuario:
    contador = 0

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        Usuario.contador += 1

    def diga_ola(self):
        print("Olá, meu nome é %s e meu email é %s" % (self.nome, self.email))



usuario2 = Usuario(nome="Nicolau", email="Niccolo369@proton.me")
print(Usuario.contador)

class Administrador(Usuario):
    def __init__(self, nome, email, chave_de_administrador):
        Usuario.__init__(self, nome, email)
        self.chave_de_administrador = chave_de_administrador

    def poder_administrador(self):
        print("Eu tenho o poder! Minha chave é %s" % self.chave_de_administrador)

usuario_adm = Administrador(nome="Admin", email="Niccolo369@proton.me",
chave_de_administrador="123456")
usuario_adm.diga_ola()
usuario_adm.poder_administrador()

class MembroStaff(Usuario):
    def __init__(self, nome, email):
        Usuario.__init__(self, nome, email)

    def diga_ola(self):
        print("Olá, meu nome é %s e eu sou membro do Staff, Em que posso ajudar" %
    (self.nome))

    membro_staff_1 = 'MembroStaff'(nome="Magnolia", email="Magnolia@proton.me")
    membro_staff_1.diga_ola()