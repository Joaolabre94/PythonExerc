"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input('Por favor informe um número inteiro: ')
def par(num):
    if num % 2 == 0:
        return True
    else:
        return False

try:
    numero = int(entrada)
    if par(numero) :
        print(f'O {numero} é par!')
    else:
        print(f'O {numero} é impar')
except:
    print('Você não digitou um número inteiro')


