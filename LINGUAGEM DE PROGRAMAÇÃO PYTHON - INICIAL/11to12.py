#11. poo - programação orientada a objetos
#criando uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")
    

pessoa1= Pessoa("João", 30)
pessoa1.saudacao()

#12 - herança: permite criar uma nova classe baseada em uma classe existente - reaproveitamento de código
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)  # chama o construtor da classe base (Pessoa)
        self.curso = curso

    def saudacao(self):
       # super().saudacao()  # chama o método saudacao da classe base
        print(f"Eu me chamo {self.nome} e estou estudando {self.curso}.")

print("--- Herança ---")
estudante1 = Estudante("Maria", 22, "Engenharia")
estudante1.saudacao()

#12 - polimorfismo: permite que diferentes classes sejam tratadas como instâncias da mesma classe base
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def saudacao(self):
        print(f"Eu sou professor {self.nome} e ensino {self.disciplina}.")

print("--- Polimorfismo ---")
professor1 = Professor("Carlos", 45, "Matemática")
pessoas = [pessoa1, estudante1, professor1]

for pessoa in pessoas:
    pessoa.saudacao()