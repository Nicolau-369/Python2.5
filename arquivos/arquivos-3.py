file = open("novo_arquivo.txt", "w")
file.write("Teste, Teste!\n")
file.write("Mais uma linha para testar")
file.close()

file = open("novo_arquivo.txt", "w")
file.write("Novo texto, mesmo arquivo")
file.close()

file = open("novo_arquivo.txt", "a")
file.write("\nTexto adicionado ao arquivo com o modo a")
file.close()

file = open("novo_arquivo.txt", "r+")
file.write("Teste r+")
file.seek(10)
file.write("Novo teste do r+")
file.close()

file.seek(0)
print(file.read())
file.close()