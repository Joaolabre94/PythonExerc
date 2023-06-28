def valores():
    resultado = int(input('Digite o numero da equação: '))
    return resultado
a = valores()
b = valores()
c = valores()

def calc_delta(a, b, c):
    delta = (b*b) - (4 * a * c)
    return delta

import math
def calc_raizes(a, b, c, delta):
    if delta < 0 :
        resultado = 'A equação não possui raízes dos números reais'
    elif delta == 0:
        x = -b / (2*a)
        resultado = f'A equação possui apenas uma raiz: {x}'
    else:
        x1 = (-b -math.sqrt(delta)) / (2*a)
        x2 = (-b +math.sqrt(delta)) / (2*a)
        resultado = f'A equação possui duas raízes: {x1}, {x2}'
    return resultado


delta = calc_delta(a, b, c)
resultado = calc_raizes(a, b, c, delta)
print(resultado)