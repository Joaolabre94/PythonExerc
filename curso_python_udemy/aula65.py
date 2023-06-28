#Calculadora a moda caceta
# Função para adicionar dois números
def add(x, y):
   return x + y

# Função para subtrair dois números
def subtract(x, y):
   return x - y

# Função para multiplicar dois números
def multiply(x, y):
   return x * y

# Função para dividir dois números
def divide(x, y):
   return x / y

def valores():
    while True:
        try:
            numero1 = float(input('Digite um número: '))
            numero2 = float(input('Digite outro número: '))
            operador = input('Digite o operador (+, -, *, /): ')
            operadores_permitidos = '+-*/'

            if operador == '+':
                final = add(numero1, numero2)
                print(f'O resultado de {numero1}+{numero2}, é: {final:.2f}')

            elif operador == '-':
                final = subtract(numero1, numero2)
                print(f'O resultado de {numero1}-{numero2}, é: {final:.2f}')

            elif operador == '*':
                final = multiply(numero1, numero2)
                print(f'O resultado de {numero1}*{numero2}, é: {final:.2f}')

            elif operador == '/':
                final = divide(numero1, numero2)
                print(f'O resultado de {numero1}/{numero2}, é: {final:.2f}')     

            if operador not in operadores_permitidos:
                print('Operador inválido.')   

            if len(operador) > 1:
                print('Digite apenas um operador.')

            while True:
                sair = input('Deseja sair? [s]im ou n[ão]: ').lower()
                if sair == 's' or sair == 'n':
                    break
                else:
                    print('Digite [s]im ou [n]ão')

            if sair == 's':
                break
        except:
            print('Um ou ambos os números são inválidos.')

valores()   