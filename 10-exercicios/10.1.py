#criar variaveis de diferentes tipo e imprimir seus valores

inteiro = 10
flutuante = 10.5
string = "Olá, mundo!"
booleano = True

print("----------------------------------------")
print(inteiro)
print(flutuante)
print(string)
print(booleano)
print("----------------------------------------")

#realizar operações aritiméticas, comparações e operadores lógicos

print(inteiro + flutuante)
print(inteiro - flutuante)
print(inteiro * flutuante)
print(inteiro / flutuante)

print(inteiro == flutuante)
print(inteiro != flutuante)
print(inteiro > flutuante)
print(inteiro < flutuante)

print(inteiro > 5 and flutuante < 15)
print(inteiro < 5 or flutuante > 15)
print("----------------------------------------")


#estruturas condicionais: escrever um programa que verifique se um número é par ou ímpar

if inteiro % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
print("----------------------------------------")


#loops: criar um programa que imprima os números de 1 a 10

for i in range(1, 11):
    print(i)
