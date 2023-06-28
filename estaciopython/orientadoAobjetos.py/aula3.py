class Pessoa:
    def __init__(self, peso, cor, nome, altura):
        self.peso = peso
        self.cor = cor
        self.nome = nome
        self.altura = altura

def exibir_informacoes_pessoa():
    pessoa1 = Pessoa(70, 'Branca', 'Maria', 165)
    print(f'Nome: {pessoa1.nome}')
    print(f'Altura: {pessoa1.altura} cm')
    print(f'Peso: {pessoa1.peso} kg')
    print(f'Cor: {pessoa1.cor}')

# Chamar a função
exibir_informacoes_pessoa()