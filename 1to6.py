#def menu - conter  1 a 4
def menu():
    print("Menu:")
    print("1- Saudações")
    print("2- Recitar poema")
    print("3- Contar piada")
    print("4- Despedida")


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

#4- def despedida
def despedida():
    print("Adeus! Até a próxima!")

#loop - chamar menu
while True:
    menu()
    opcao = input("Escolha uma opção (1-4): ")
    if opcao == "1":
        saudações()
    elif opcao == "2":
        recitar_poema()
    elif opcao == "3":
        contar_piada()
    elif opcao == "4":
        despedida()
        break
    else:
        print("Opção inválida. Tente novamente.")