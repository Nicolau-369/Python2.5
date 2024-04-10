class main:
    pass

from cliente import cliente

from conta import conta

c1= cliente("nicolau", "0800-222-4444")
conta=conta(c1.get_nome(), 1222)

conta.deposita(100)
conta.saque(50)
conta.extrato()