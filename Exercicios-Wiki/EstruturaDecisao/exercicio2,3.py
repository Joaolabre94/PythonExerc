#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# def valores():
#     resultado = int(input('Escreva o valor desejado: '))
#     if resultado >= 0:
#         return 'Positivo!'
#     else:
#         resultado < 0
#         return 'Negativo!'
# print(f'O seu valor é {valores()}')

def valores():
    while True:
        try:
            valor = float(input('Digite o valor desejado: '))
            if valor >= 0:
                print(f'O numero {valor:.2f} é positivo!')
                break
            else:
                print(f'O {valor} é negativo!')
                break
        except:
            print(f'Digite um valor correto!')
valores()