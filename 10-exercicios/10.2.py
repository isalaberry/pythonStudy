#crie uma funcao que receba dois numeros e retorne sua soma
def somar_dois_numeros(num1, num2):
    return num1 + num2

print(somar_dois_numeros(5, 10))

#importe o modulo math e use a função sqrt para calcular a raiz quadrada de um numero
from math import sqrt
num1 = 16
print(sqrt(num1))

#manipula uma string para deixa-la em maiusculas e depois fatie
string = "Olá, mundo!"
print(string.upper())
print(string[0:5])

#escreva um programa que salve uma lista de nomes em um arquivo e depois leia o conteudo desse arquivo
nomes = ["Alice", "Bob", "Charlie"]
with open("nomes.txt", "w") as arquivo:
    for nome in nomes:
        arquivo.write(nome + "\n")

with open("nomes.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)