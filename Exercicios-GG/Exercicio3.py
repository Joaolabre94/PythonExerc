# 3) Faça um programa que leia um valor inteiro de até 4 algarismos e calcule a soma dos 
# algarismos desse número. Caso o valor informado seja maior que 4 algarismos, emita 
# um erro. Exemplo:
# Informe um número:
# 3267
# Soma dos algarismos do número:
# 18

def calcular_soma_algarismos(numero):
    soma = 0
    for caractere in numero:
        soma = soma + int(caractere)
    return soma

def valores():
    while True:
        try:
            valor = input('Digite um valor inteiro até 4 algarismos: ')
            if len(valor) <= 4:
                resultado = calcular_soma_algarismos(valor)
                print(f'A soma desses algarimos é: {resultado}')
                break
        except:
            print('Você informou mais de 4 algarismos, ou não foi números inteiros, informe o valor correto.')


valores()