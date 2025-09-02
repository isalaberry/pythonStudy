#def menu - conter  1 a 4
def menu():
    print("Menu:")
    print("1- Saudações")
    print("2- Recitar poema")
    print("3- Contar piada")
    print("4- Cálculos")
    print("5- Lógica")
    print("6- Idade")
    print("7- Despedida")


#1- def saudações
def saudações():
    nome = input("Qual é o seu nome? ")
    print("Olá, " + nome + "! Como você está?")

#2- def recitar poema
def recitar_poema():
    print("Todas as cartas de amor são ridículas.")
    print("Não seriam cartas de amor se não fossem ridículas.")

#3- def contar piada
def contar_piada():
    print("Por que a galinha atravessou a rua?")
    print("Para chegar do outro lado.")

#4- cálculos
def calculos():
    a = float(input("Insira a variável a: ")) #precisa converter para float
    b = float(input("Insira a variável b: "))
    print("A soma de a e b é:", a + b)
    print("A subtração de a e b é:", a - b)
    print("A multiplicação de a e b é:", a * b)
    print("A divisão de a e b é:", a / b)
    print("A divisão inteira de a por b é:", a // b)
    print("O módulo da divisão de a por b é:", a % b)
    print("A exponenciação de a por b é:", a ** b)

#5- def lógica
def logica():
    a = input("Insira o valor lógico (True/False) de a: ").strip().lower() == "true" #precisa converter para booleano
    #Se você digitar True, o código faz: "True".strip().lower() == "true" → "true" == "true" → retorna True (tipo bool).
    #Se você digitar False, o código faz: "False".strip().lower() == "true" → "false" == "true" → retorna False
    b = input("Insira o valor lógico (True/False) de b: ").strip().lower() == "true"
    print("A conjunção de a e b é:", a and b)
    print("A disjunção de a e b é:", a or b)
    print("A negação de a é:", not a)

#6- def idade
def idade():
    ano_nascimento = int(input("Insira o ano do seu nascimento: ")) #precisa converter para inteiro
    ano_atual = int(input("Insira o ano atual: "))
    idade = ano_atual - ano_nascimento
    if idade < 0:
        print("Ano de nascimento inválido.")
    elif idade <= 13:
        print("Você é uma criança.")
    elif idade <= 20:
        print("Você é um adolescente.")
    elif idade <= 60:
        print("Você é um adulto.")
    else:
        print("Você é velho.")


#7- def despedida
def despedida():
    print("Adeus! Até a próxima!")



#loop - chamar menu
while True:
    print("----------------------------------------")
    menu()
    opcao = input("Escolha uma opção (1-7): ")
    print("----------------------------------------")
    if opcao == "1":
        saudações()
    elif opcao == "2":
        recitar_poema()
    elif opcao == "3":
        contar_piada()
    elif opcao == "4":
        calculos()
    elif opcao == "5":
        logica()
    elif opcao == "6":
        idade()
    elif opcao == "7":
        despedida()
        break
    else:
        print("Opção inválida. Tente novamente.")