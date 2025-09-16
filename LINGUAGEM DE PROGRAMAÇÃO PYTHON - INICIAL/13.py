try:
    numero=int(input("Insira um número: "))
    print(f"O número digitado foi {numero}")
except ValueError:
    print("Valor inválido! Por favor, insira um número inteiro.")


try:
    arquivo=open("arquivo.txt","r")
    conteudo=arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado!")
finally:
    print("Execução finalizada.")


def dividir(a,b):
    if b==0:
        raise ValueError("Divisor não pode ser zero.")  
    return a/b
try: 
    resultado=dividir(numero,0)
    print(f"Resultado da divisão: {resultado}")
except ValueError as e:
    print(f"Erro na divisão: {e}")
