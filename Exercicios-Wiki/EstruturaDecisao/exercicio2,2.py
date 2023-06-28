#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def resultado(a):
    if a >= 0:
        return 'positivo'
    else:
        return 'negativo'

def valor():
    resultado1 = float(input('Esreva o valor desejado: '))
    final = resultado(resultado1)
    print(f'O número é: {final}')

valor()