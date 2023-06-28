"""
Faça um programa que peça ao usuário para digitar um dois números  inteiros, some eles e 
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
            valor1 = int(input('Digite o primeiro número: '))
            valor2 = int(input('Digite o segundo número: '))
            soma = valor1 + valor2
            numero = soma 
            if par(numero):
                print(f'A soma do valor {valor1} + {valor2} ficou {soma} que é par!')
                break
            else:
                print(f'A soma do valor {valor1} + {valor2} ficou {soma} que é impar!')
                break
        except:
            print(f'O número informado não é inteiro.')

resultado()