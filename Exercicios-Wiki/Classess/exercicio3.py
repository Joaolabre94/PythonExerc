#Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudar_valor_lados(self, novoLadoA, novoLadoB):
        self.ladoA = novoLadoA
        self.ladoB = novoLadoB
        
    def retornar_valor_lados(self):
        return self.ladoA, self.ladoB

    def calcular_area(self):
        self.area = self.ladoA * self.ladoB
    
    def calcular_perimetro(self):
        self.perimetro = (self.ladoA * 2) + (self.ladoB * 2)

def main():
    while True:
        try:
            ladoA = float(input("Informe o valor do lado A: "))
            ladoB = float(input("Informe o valor do lado B: "))
            retangulo = Retangulo(ladoA, ladoB)
            retangulo.calcular_area()
            retangulo.calcular_perimetro()
            print(f"Área do retângulo: {retangulo.area}")
            print(f"Perímetro do retângulo: {retangulo.perimetro}")

            area_piso = float(input("Informe a área do piso em metros quadrados: "))
            area_rodape = float(input("Informe a área do rodapé em metros quadrados: "))
            quantidade_pisos = retangulo.area / area_piso
            quantidade_rodapes = retangulo.perimetro / area_rodape
            print("Quantidade de pisos necessários:", quantidade_pisos)
            print("Quantidade de rodapés necessários:", quantidade_rodapes)
            break
        except:
            print('Digite um número corretamente.')
if __name__ == '__main__':
    main()