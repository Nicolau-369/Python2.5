# Demonstração das funções de string templates
from string import Template


def main():
    # Formatação tradicional usando o método format()
    frase = "Treinamento {0} com {1}".format(
        "Python Intermediário", "Nicolau Salvatore")
    print(frase)

    # Crie um template com placeholders
    templ = Template("Treinamento ${Linguagem} com ${Programador}")

    # Use o método substitute passando argumentos nomeados
    frase_2 = templ.substitute(
        Linguagem="Python Intermediário",
        Programador="Nicolau Salvatore"
    )
    print(frase_2)

    # Use  o método substitute com um dicionário
    dados = {
        "Programador": "Nicolau Salvatore",
        "Linguagem": "Python Intermediário"
    }
    frase_3 = templ.substitute(dados)
    print(frase_3)


if __name__ == "__main__":
    main()