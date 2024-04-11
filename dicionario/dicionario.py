aluno = {"nome": "Nicolau", "Idade": 54, "nota": 9.2 }
print(aluno)

dict_vazio = {}
print(dict_vazio)

print(aluno["nome"])
print(aluno["Idade"])

aluno["nota"] = 8.2
aluno["peso"] = 74
print(aluno)

del aluno["Idade"]
print(aluno)
aluno.clear()
print(aluno)

aluno = {"nome": "Nicolau", "Idade": 54, "nota": 9.2}
print(len(aluno))

print("idade" in aluno)
print("peso" in aluno)

aluno = {"nome": "Nicolau", "Idade": 54, "nota": 9.2}
print(aluno.get("nome"))
print(aluno.get("peso"))
print(aluno.get("peso", "Não existe"))

print(aluno.items())
print(aluno.keys())
print(aluno.values())

aluno_original = {"nome": "Nicolau", "idade": 54, "nota": 9.2}
aluno_update = {"peso": 75, "nota": 8.7}
aluno_original.update(aluno_update)
print(aluno_original)