aluno = {"nome": "Magnólia", "Idade": 25, "nota": 9.8}

print("Exemplo 1a - iterando sobre chaves")
for chave in aluno:
    print(chave)

print("\nExemplo 1b - iterando sobre chaves")
for chave in aluno.keys():
    print(chave)

print("\nExemplo 2 - iterando sobre valores")
for valor in aluno.values():
    print(valor)

print("\nExemplo 3 - iterando sobre ambos")
for chave, valor in aluno.items():
    print(chave + "-" + str(valor))

print("Range com 1 parâmetro")
for i in range(5):
    print(i)

print("Range com 2 parâmetros")
for i in range(3,10):
    print(i)