#Calculadora 2.0

def calculo(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
       return  num1 * num2
    elif operador == '/':
        return num1 / num2
    elif operador == '^':
        return num1 ** num2     

def valores():
    while True:
        try:
            num1 = float(input('Digite um número: '))
            operador = input('Digite um operador (+, -, *, /, ^): ')
            while operador not in '+-*/^':
                operador = input('Digite um operador corretamente (+, -, *, /, ^): ')
            num2 = float(input('Digite outro número: '))

            resultado = calculo(num1, num2, operador)
            print(f'O resultado de {num1} {operador} {num2} é: {resultado:.2f}')

            while True:
                sair = input('Deseja sair? [s]im ou [n]ão: ').lower()
                if sair == 's' or sair == 'n':
                    break
                else:
                    print('Digite [s]im ou [n]ão')
            if sair == 's':
                break

        except:
            print('Você voltou para o começo, digite números corretos.')

valores()            