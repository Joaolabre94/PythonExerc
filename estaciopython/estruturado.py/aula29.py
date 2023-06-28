#Implementar uma solução em Python que faça o tratamento de exceção de divisão por zero
def dividir(x,y):
    try:
        valor = x / y
        print(f'A resposta é: {valor}')
    except ZeroDivisionError:
        print('Divisão por zero')

dividir(3, 0)
dividir(3, 2)