# Usando a classe Counter
from collections import Counter


def main():
    # Uma lista de estudantes na turma A
    turma_a = ["Malik", "Nicolau", "Magnolia", "Josias", "Morgana", "Andromeda"
               "Maria", "Rex", "Kletus", "Trask", "Medici", "Sun"]

    # Uma lista de estudantes na turma B
    turma_b = ["Lorenzo", "Joaquim", "Joaquina", "Suelen", "Joãozinho", "Gabriela",
               "Leticia", "Valdemir", "Walter", "Bianca", "Tati", "Neusa"]

    # Crie um Counter para as turmas A e B
    a = Counter(turma_a)
    b = Counter(turma_b)

    # Quantos estudantes na turma A se chamam Nicolau?
    print(a["Nicolau"])

    # Quantos estudantes estão na turma A?
    print(sum(a.values()), "estudantes na turma A")

    # Combine as duas turmas
    a.update(turma_b)
    print(sum(a.values()), "estudantes na turma B")

    # Quais os 3 nomes mais comuns nas duas turmas?
    print(a.most_common(3))

    # Separe as duas turmas e mostre o nome mais comum da turma a
    a.subtract(turma_b)
    print(a.most_common(3))

    # Qual a intersecção de nomes entre as duas turmas?
    print(a & b)


if __name__ == "__main__":
    main()
