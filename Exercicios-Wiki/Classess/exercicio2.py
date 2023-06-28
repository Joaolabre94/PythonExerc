# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado
    
    def mudar_valor_do_lado(self, novolado):
        self.tamanho_do_lado = novolado

    def retornar_valor_do_lado(self):
        return self.tamanho_do_lado

    def calcular_area(self):
        return self.tamanho_do_lado ** 2


    def atributos_quadrado(self):
        print(f'O lado do quadrado é: {self.tamanho_do_lado}')


quadrado = Quadrado(6)

quadrado.atributos_quadrado()

quadrado.mudar_valor_do_lado(10)

print(f'Novo lado do quadrado é: {quadrado.retornar_valor_do_lado()}')

print(f'A área desse quadrado é: {quadrado.calcular_area()}')