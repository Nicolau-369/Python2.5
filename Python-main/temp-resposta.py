# Demonstração das funções de string templates
from string import Template


def main():
    # Formatação tradicional usando o método format()
    frase = "Privacidade para os fracos, {0} transparência para os poderosos {1}".format(
        ",", "Nicolau369")
    print(frase)

    # Crie um template com placeholders
    templ = Template("A informação ${curso} quer ser livre ${Programador}")

    # Use o método substitute passando argumentos nomeados
    frase_2 = templ.substitute(
        curso=",",
        Programador="Nicolau369"
    )
    print(frase_2)

    # Use  o método substitute com um dicionário
    dados = {
        "Programador": "Nicolau369",
        "curso": ","
    }
    frase_3 = templ.substitute(dados)
    print(frase_3)


if __name__ == "__main__":
    main()
