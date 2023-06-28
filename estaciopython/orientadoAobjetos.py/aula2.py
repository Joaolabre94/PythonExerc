# class Pessoa:
#     def __init__(self, nome, ender):
#         pessoa1 = Pessoa('maria', 'rua 01234')
#         pessoa2 = Pessoa('joão', 'Rua 56789')

#         print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}')
#         print(f'Nome: {pessoa2.get_nome()}, Endereço: {pessoa2.get_ender()}')


class Pessoa:
    def __init__(self, nome, ender):
        self.nome = nome
        self.ender = ender

    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender

class Empresa:
    def __init__(self, nome, ender):
        self.nome = nome
        self.ender = ender

    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender

empresa1 = Empresa('Pratic', 'Rua01234')
empresa2 = Empresa('LD', 'Rua 56789')
# Criar instâncias da classe Pessoa
pessoa1 = Pessoa('Maria', 'Rua 01234')
pessoa2 = Pessoa('João', 'Rua 56789')

# Imprimir as informações na tela
print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}')
print(f'Nome: {pessoa2.get_nome()}, Endereço: {pessoa2.get_ender()}')
print(f'Nome: {empresa1.get_nome()}, Endereço: {empresa1.get_ender()}')
print(f'Nome: {empresa2.get_nome()}. Endereço: {empresa2.get_ender()}')