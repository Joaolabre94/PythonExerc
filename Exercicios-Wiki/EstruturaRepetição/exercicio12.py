# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50
valor = int(input('Digite o númreo da tabuada que gostaria de saber de 1 ao 10: '))
if valor >= 1 and valor <= 10:
    print(f'Tabuada de {valor}')
    for x in range(1, 11):
        resultado = x * valor
        print(f'{valor} X {x} = {resultado}')

else:
    print('Número inválido. Digite um número entre 1 e 10.')