#Faça um Programa que leia três números e mostre o maior e o menor deles.
def calc(a, b, c):
    maior = max(a, b, c)
    menor = min(a, b, c)
    return maior, menor

def valores():
    while True:
        try:
            num1 = float(input('Informe o primeiro número: '))
            num2 = float(input('Informe o segundo número: '))
            num3 = float(input('Informe o terceiro número: '))
            total = calc(num1, num2, num3)
            print(f'O maior número é: {total[0]}')
            print(f'O menor número é: {total[1]}')
            break

        except:
            print('Digite o valor correto.')

valores()