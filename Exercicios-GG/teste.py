# faça a soma de uma lista escrita por um usuario,

def soma_lista(num):
    soma = 0
    for caractere in num:
        soma = soma + int(caractere)
    return soma
    
def valores():
    while True:
        try:
            lista = input('Escreve uma lista com número, exemplo 456143: ')
            if soma_lista(lista):
                resultado = soma_lista(lista)
                print(f'O resultado da soma da sua lista é: {resultado}')
                break
        except:
            print('Digite o valor corretamente')


valores()