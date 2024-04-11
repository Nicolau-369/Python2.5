lista1 = ["Nicolau", "Malik", "Kletus", "Magnólia", "Morgana", "Andromeda"]
set1 = set(lista1)
set2 = {"Dragão", "Fênix", "Harpia", "Dragão", "Leão", "Raposa", "Gavião"}
print(set2)

set3 = set("Raposa")
print(set3)

lista2 = ["Nicolau", "Malik", "Kletus", "Trask", "Magnólia", "Morgana", "Andromeda"]
lista_sem_duplicates = list(set(lista2))
print(lista_sem_duplicates)

print(set2)
set2.remove("Harpia")
print(set2)

print(len(set2))
print("gato" in set2)
print("Porco" in  set2)

set4 = {"Malik", "Nicolau", "Maria", "Kletus", "Trask"}
set5 = {"Maria", "Andromeda", "Josias", "Trask"}
print(set4.difference(set5))
print(set4.intersection(set5))

set_backup = set4
print(set_backup)
set4.clear()
print(set_backup)

set4 = {"Malik", "Nicolau", "Maria", "Kletus", "Trask"}
set_backup = set4.copy()
print(set_backup)
set4.clear()
print(set_backup)