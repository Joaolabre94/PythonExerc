"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
def par(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def resultado():
    while True:
        try:
            resultado = int(input('Digite um número inteiro: '))
            if par(resultado):
                print(f'O número {resultado} é par!')
                break
            else:
                print(f'O número {resultado} é impar!')
                break
        except:
            print('Por favor, digite um número inteiro corretamente.')
resultado()