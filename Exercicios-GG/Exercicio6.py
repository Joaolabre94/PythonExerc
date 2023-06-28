# 6) Escreva um programa que receba três números e determina qual é o maior.
def resultado(a, b, c):
    if a > b or a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def valores():
    while True:
        try:
            a = int(input('Digite um número inteiro: '))
            b = int(input('Digite um segundo número inteiro: '))
            c = int(input('Digite um terceiro número inteiro: '))
            resultado(a, b, c)
            final = resultado(a, b, c)
            print(f'O seu maior número é: {final}')
            break
        except:
            print('Digite o número correto.')

valores()