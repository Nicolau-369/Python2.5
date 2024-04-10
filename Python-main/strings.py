def saque(self, valor):
    if self.saldo>=valor:
        self.saldo-=valor
        print("saque realizado com sucesso")
    else:
        print("saldo insuficiente")

def deposita (self, valor):
    self.saldo=valor

def extrato (self):
    print("cliente: ", self.titular, "saldo atual: ", self.saldo)