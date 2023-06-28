def calcular(numero1, numero2, operador):
    if operador == '+':
        return numero1 + numero2
    elif operador == '-':
        return numero1 - numero2
    elif operador == '*':
        return numero1 * numero2
    elif operador == '/':
        return numero1 / numero2
    else:
        print('Operador inválido')

def valores():
    while True:
        try:
            numero1 = float(input('Digite um número: '))
            numero2 = float(input('Digite outro número: '))
            operador = input('Digite o operador (+, -, *, /): ')
            operadores_permitidos = '+-*/'
            
            resultado = calcular(numero1, numero2, operador)
            print(f'O resultado de {numero1} {operador} {numero2} é: {resultado:.2f}')
        
            if operador not in operadores_permitidos:
                print('Operador inválido.')   

            if len(operador) > 1:
                print('Digite apenas um operador.')

            while True:
                sair = input('Deseja sair? [s]im ou [n]ão: ').lower()
                if sair == 's' or sair == 'n':
                    break
                else:
                    print('Digite [s]im ou [n]ão')

            if sair == 's':
                break

        except :
            print('Um ou ambos os números são inválidos.')

valores()