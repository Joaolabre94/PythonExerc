def par(x):
    if x%2 == 0:
        return True
    else:
        return False
    
def valores():
    while True:
        try:
            valor1 = int(input('Digite um valor: '))
            valor2 = int(input('Digite outro valor: '))
            soma = valor1 + valor2
            if par(soma):
                print(f'A soma dos seus valores é: {soma}, e é: Par')
            else:
                print(f'A soma dos seus valores é: {soma}, e é: Ímpar!')
            break

        except:
            print('Digite um valor correto.')

valores()