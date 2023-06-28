#Exemplo1: Implementar uma solução em python que calcule as raízes de uma equação do segundo grau.
#Exemplo: dada a equação x**2 + 5x + 6 = 0 as raizes são {-3, -2}


def entrada_dados():
    coeficiente  = int(input('Digite o valor do coeficiente: '))
    return coeficiente

a=entrada_dados()
b=entrada_dados()
c=entrada_dados()

def calc_delta(a, b, c):
    delta = b*b - 4*a*c
    return delta

import math
def calcular_raizes (a,b,c,delta):
    if delta < 0:
        resultado = 'a equação não possui raízes dos números reais'
    elif delta == 0:
        x = -b / (2*a)
        resultado = f'a equação possui apenas a raiz: {x}'
    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        resultado = f'a equação possui as raízes: {x1}, {x2}'
    return resultado

delta = calc_delta(a, b, c)
resultado = calcular_raizes (a, b, c, delta)
print(resultado)

