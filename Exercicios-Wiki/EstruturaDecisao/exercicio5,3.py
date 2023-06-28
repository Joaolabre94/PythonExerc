#Faça um programa para a leitura de duas notas parciais de um aluno. 
#O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
def calc(x):
    if x == 100:
        return 'Aprovado com distinção'
    elif x >= 70:
        return 'Aprovado'
    else:
        return 'Reprovado'

def valores():
    while True:
        try:
            nota1 = float(input('Digite a primeira nota: '))
            nota2 = float(input('Digite a segunda nota: '))
            media = (nota1 + nota2) / 2
            final = calc(media)
            print(f'Você foi: {final}')
            break
        
        except:
            print('Digite um valor correto.')

valores()