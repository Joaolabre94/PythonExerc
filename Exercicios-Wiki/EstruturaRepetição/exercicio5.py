# Altere o programa anterior permitindo ao usuário informar as 
# populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
import math
def valores():
    while True:
        try:
            populaçaoA = int(input('Digite a população do pais A: '))
            populaçaoB = int(input('Digite a população do pais B: '))
            crescimentoA = float(input('Digite a taxa de crescimento anual do País A: '))
            crescimentoB = float(input('Digite a taxa de crescimento anual do País B: '))

            anos = 0

            if populaçaoA < populaçaoB:
                while populaçaoA < populaçaoB:
                    populaçaoA = populaçaoA * crescimentoA
                    populaçaoB = populaçaoB * crescimentoB
                    anos += 1
                print(f'Vai levar {anos} anos para o País A alcançar o País B')
                

            elif populaçaoA > populaçaoB:
                while populaçaoA > populaçaoB:
                    populaçaoA = populaçaoA * crescimentoA
                    populaçaoB = populaçaoB * crescimentoB
                    anos += 1
                print(f'Vai levar {anos} anos para o País B alcançar o País A')
                

            else:
                print('As populações já são iguais.')
                

            while True:
                sair = input('Deseja sair? [s]im ou [n]ão: ').lower()
                if sair == 's' or sair == 'n':
                    break
                else:
                    print('Digite [s]im ou [n]ão')
            if sair == 's':
                break

        except:
            print('Digite valores corretamente.')

valores()