#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
def valores():
    while True:
        try:
            raio = float(input('Digite o raio do círculo desejado: '))
            x = math.pi * (raio**2)
            print(f'A área do seu circulo é: {x:.2f}')
            break
        except:
            print(f'Por favor, digite o raio corretamente.')

valores()