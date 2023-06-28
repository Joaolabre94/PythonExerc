class Pessoa:
    def __init__(self, peso, cor, nome, altura):
        self.peso = peso
        self.cor = cor
        self.nome = nome
        self.altura = altura

def solicitar_informacoes_pessoa():
    peso = input("Digite o peso da pessoa: ")
    cor = input("Digite a cor da pessoa: ")
    nome = input("Digite o nome da pessoa: ")
    altura = input("Digite a altura da pessoa: ")

    pessoa = Pessoa(peso, cor, nome, altura)
    return pessoa

def exibir_informacoes_pessoa(pessoa):
    print(f'Nome: {pessoa.nome}')
    print(f'Altura: {pessoa.altura} cm')
    print(f'Peso: {pessoa.peso} kg')
    print(f'Cor: {pessoa.cor}')
# Solicitar as informações da pessoa
pessoa = solicitar_informacoes_pessoa()

# Exibir as informações da pessoa
exibir_informacoes_pessoa(pessoa)