"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

def valores():
    while True:
        try:
            entrada = (input('Informe a hora: '))
            hora = int(entrada)
            if hora >= 0 and hora <= 12:
                print('Bom dia!')
                break
            elif hora >= 13 and hora <= 18:
                print('Boa tarde!')
                break
            elif hora >= 19 and hora <= 23:
                print('Boa noite!')
                break
            else:
                print('Não conheço essa hora, digite a hora correta')               
        except:
            print('Por favor, digite somente números inteiros!')
valores()