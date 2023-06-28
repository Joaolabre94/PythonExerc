# 7) Modifique o programa anterior para imprimir os números em ordem crescente.


def resultado1(a, b, c ):
    if a > b and a > c and b > c:
        return c, b, a
    elif b > a and b > c and a > c:
        return c, a, b
    elif a > b and a > c and c > b:
        return b, c, a
    elif b > a and b > c and c > a:
        return a, c, b
    elif c > a and c > b and a > b:
        return b, a, a
    elif c > a and c > b and b > a:
        return a, b, c

# ou

def resultado2(a, b, c):
    numeros = a, b, c
    numeros_ordenados = sorted(numeros)
    return numeros_ordenados





def valores():
    while True:
        try:
            a = int(input('Digite um número inteiro: '))
            b = int(input('Digite um segundo número inteiro: '))
            c = int(input('Digite um terceiro número inteiro: '))
            resultado2(a, b, c)
            final = resultado2(a, b, c)
            print(f'Os numeros em ordem crescente fica: {final}')
            break
        except:
            print('Digite o número correto.')

valores()