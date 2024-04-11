print("Vamos dividir dois números inseridos por você\n")
num1 = input("Insira o primeiro número: ")
num2 = input("Insira o segundo número: ")

resultado = int(num1) / int(num2)
print("O resultado é " + str(resultado))

print("Vamos dividir dois números inseridos por você\n")
num1 = input("Insira o primeiro número: ")
num2 = input("Insira o segundo número: ")

try:
    resultado = int(num1) / int(num2)
    print("O resultado é " + str(resultado))
except ZeroDivisionError:
    print("O segundo número não pode ser zero")
except ValueError:
    print("Você deve inserir dois números")

try:
    resultado = int(num1) / int(num2)
    print("O resultado é " + str(resultado))
except:
    print("Uma das entradas é inválida. Favor inserir dois números, sendo o segundo diferente que zero")

try:
    resultado = int(num1) / int(num2)
    print("O resultado é " + str(resultado))
except ZeroDivisionError:
    print("Você deve inserir dois números")
else:
    print("Divisão feita!")

try:
    resultado = int(num1) / int(num2)
    print("O resultado é " + str(resultado))
except ZeroDivisionError:
    print("O Segundo número não pode ser zero")
except ValueError:
    print("Você deve inserir dois números")
finally:
    print("Programa concluído")