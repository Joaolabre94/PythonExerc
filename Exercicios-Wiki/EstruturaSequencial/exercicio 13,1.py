# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

def valores():
    while True:
        try:
            altura = float(input('Digite a sua altura: '))
            sexo = input('Digite seu sexo [h]omem e [m]ulher: ').lower()
            homem = (72.7 * altura) - 58
            mulher = (62.1 * altura) - 44.7
            if sexo == 'h':
                print(f'Seu peso ideal como homem é: {homem}')
            elif sexo == 'm':
                print(f'Seu peso ideal como mulher té: {mulher}')
                break
            else:
                print('Digite valores corretos.')
            
        except:
            print('Digite valores corretos.')

valores()