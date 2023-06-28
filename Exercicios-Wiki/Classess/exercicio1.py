# Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor(self, novacor):
        self.cor = novacor
    
    def mostraCor(self):
        return self.cor
    
    def mostraAtributos(self):
        print(f'Cor: {self.cor}')
        print(f'Circunferência: {self.circunferencia}')
        print(f'Material: {self.material}')

# Criar uma instância da classe Bola
bola = Bola('Azul', 10, 'Borracha')

# Exibir os atributos da bola
bola.mostraAtributos()

# Trocar a cor da bola
bola.trocaCor('Vermelho')

# Exibir a nova cor da bola
print(f'Nova cor da bola: {bola.mostraCor()}')