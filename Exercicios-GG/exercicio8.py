# Faça um programa que receba os três coeficientes de uma equação de segundo grau 
# (a, b, c) e determine as raízes. Considere o caso em que o delta de Bhaskara é negativo.

import math

def calcular_delta(num1, num2, num3):
    x = (num2**2) - (4*num1*num3)
    return x

def valores():
    while True:
        try:
            num1 = int(input('Digite o primeiro número: '))
            num2 = int(input('Digite o segundo número: '))
            num3 = int(input('Digite o terceiro número: '))
            delta = calcular_delta(num1, num2, num3)

            if delta > 0:
                x1 = (-num2 + math.sqrt(delta)) / (2*num1)
                x2 = (-num2 - math.sqrt(delta)) / (2*num1)
                print(f'O valor de da equação possui duas raízes reais e diferentes, sendo x1: {x1}, e x2: {x2}')
            elif delta == 0:
                x1 = (-num2 ) / (2*num1)
                print(f'O valor de da equação possui duas raízes reais e iguais, sendo x1: {x1}, e x2: {x1}')
            else:
                print('Não possui solução real!')
            break
            
        except:
            print('Digite valors corretos')
valores()