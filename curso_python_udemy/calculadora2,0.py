def calculos(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '/':
        return num1 / num2
    elif operador == '*':
        return num1 * num2
    elif operador == '^':
        return num1 ** num2


def valores():
    while True:
        try:
            num1 = float(input('Digite o primeiro número: '))
            operador = input('Digite um operador (+, -, /, *, ^): ')
            while operador not in '+-/*^':
                operador = input('Digite um operador corretamente (+, -, /, *, ^): ')
            num2 = float(input('Digite o segundo número: '))

            total = calculos(num1, num2, operador)
            print(f'{num1} {operador} {num2} é: {total:.2f}')

            while True:
                sair = input('Deseja sair? [s]im ou [n]ão: ').lower()
                if sair == 's' or sair == 'n':
                    break
                else:
                    print('Digite [s]im ou [n]ão')
            if sair == 's':
                break
        except:
            print('Você voltou para o início, digite um valor correto dessa vez.')

valores()