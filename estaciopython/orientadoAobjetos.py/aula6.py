#Método dde classe x método estático
from datetime import date
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    #Um método de classe para criar
    #Um objeto pessoa através do ano de nascimento
    @classmethod
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)
    #Método Estático: verificar se é maior de idade
    @staticmethod
    def ehMaiorIdade(idade):
        return idade >= 18
    
pessoa1 = Pessoa('Maria', 26)
pessoa2 = Pessoa.apartirAnoNascimento('ana', 2006)
print(pessoa1.idade)
print(pessoa2.idade)
#Imprimir o resultado
print(Pessoa.ehMaiorIdade(17))