# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com 
# as mensagens adequadas.

def valores():
    while True:
        try:
            peso = int(input('Digite quantos quilos em números inteiros o peixe possui: '))
            limite = 50
            excesso = 0
            multa = 0
            if peso > limite:
                excesso = peso - limite
                multa = excesso * 4
                print(f'O quilo dos peixes: {peso}, ele passou do limite que é: {limite}, com isso você ganhou uma multa de: {multa} ')
                break
            else:
                print(f'O quilo dos peixes: {peso}, não ultrapassou o limite de: {limite} e por isso não receberá multas')
                break
        except:
            print('Digite valores corretos.')


valores()