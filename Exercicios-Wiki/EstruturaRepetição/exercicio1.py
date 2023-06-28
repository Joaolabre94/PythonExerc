#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
#seja inválido e continue pedindo até que o usuário informe um valor válido.
def valores():
    while True:
        valor = float(input('Informe um valor de 0 a 10: '))
        if valor in range(0,10):
            print(f'Valor Valido: {valor}')
            break
        else:
            print(f'Valor Inválido: {valor}')
valores()

