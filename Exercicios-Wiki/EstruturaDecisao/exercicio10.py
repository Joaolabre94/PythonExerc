#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
while True:
    matutino = input('Qual turno você estuda, [M]-matutino; [V]-verpestino; [N]-noturno: ').lower()
    if matutino == 'm':
        print('Bom dia!')
        break
    elif matutino == 'v':
        print('Boa tarde!')
        break
    elif matutino == 'n':
        print('Boa noite')
        break
    else:
        print('Valor inválido!')

