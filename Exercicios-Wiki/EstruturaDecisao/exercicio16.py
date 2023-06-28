# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math

def delta(a, b, c):
    resultado = (b**2) - (4*a*c)
    return resultado

def equaçao2_grau():
    while True:
        try:
            a = int(input('Digite o valor de "a": '))
            if a == 0:
                print('A equação não é de segundo grau, programa encerrado.')
                break
            b = int(input('Digite o valor de "b": '))
            c = int(input('Digite o valor de "c": '))
            calculo_delta = delta(a,b,c)
            if calculo_delta < 0:
                print('A equação não possui raizes reais, programa encerrado.')
            elif calculo_delta == 0:
                x = -b / (2*a)
                print(f'Sua função possui apenas uma reaiz real, resultando em: {x:.2f}')
            else:
                raiz = math.sqrt(calculo_delta)
                x1 = (-b + raiz) / (2*a)
                x2 = (-b - raiz) / (2*a)
                print(f'A sua equação possui duas raizes reais, sendo respectivamente \nA primeira raiz: {x1:.2f} \nA segunda raiz: {x2:.2f}')
            break
        except:
            print('Digite somente números.')
            
equaçao2_grau()