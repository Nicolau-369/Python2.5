alunos = ["Nicolau", "Malik", "Magnólia"]
notas = [9.5, 9.2, 7.5]
print(alunos)
print(notas)
lista_vazia = []
print(lista_vazia)

lista_misturada = [12, 15.56, "Sorveteria", ["Baunilha", "Chocolate"]]
print(lista_misturada)

print(alunos[0])
print(notas[2])

print(alunos[-1])
print(alunos[-3])

print(notas)
notas[2] = 7.7
print(notas)

print(alunos)
alunos.append('Zak')
print(alunos)

print(alunos)
alunos.insert(1, "Maria")
print(alunos)

print(alunos)
novos_alunos = ['Josias', 'Maria', 'Morgana']
alunos.extend(novos_alunos)
print(alunos)

alunos1 = ['Malik', 'Nicolau', 'Malik']
alunos2 = ['Josias', 'Kletus', 'Trask']
print(alunos1 + alunos2)

print(notas*2)

print(alunos)
alunos.remove('Josias')
print(alunos)

print(alunos)
aluno_removido = alunos.pop()
print(aluno_removido)
print(alunos)
aluno_removido = alunos.pop(2)
print(aluno_removido)
print(alunos)

alunos = ['Nicolau', 'Malik', 'Morgana', 'Andromeda', 'Kletus', 'Josias', 'Trask']
print(alunos)
alunos.remove('Kletus')
print(alunos)

print(alunos)
print(alunos[0:2])
print(alunos[2:4])
print(alunos[2:5])

print(alunos[:3])
print(alunos[3:])

print(alunos[1:-1])
print(alunos[2:-2])

print(len(alunos))

print(max(notas))
print(min(notas))

alunos = ["Nicolau", "Malik", "Kletus", "Trask"]
alunos_backup = alunos
print(alunos_backup)
alunos.clear()
print(alunos_backup)

alunos = ["Nicolau", "Malik", "Kletus", "Trask", "Magnólia", "Andromeda", "Morgana"]
alunos_backup = alunos.copy()
alunos.clear()
print(alunos_backup)

alunos.extend(['Maria', 'Josias', 'Calisto'])
print(alunos.count('Maria'))

alunos.sort()
print(alunos)

alunos.reverse()
print(alunos)

print("Kletus" in alunos)
print("Trask" in alunos)

alunos_string = "; ".join(alunos)
print(alunos_string)
alunos_lista = alunos_string.split("; ")
print(alunos_lista)