# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
# A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” 
# se o conceito for D ou E.
nota1 = int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
media1 = (nota1 + nota2) /2
media2 = 0
notas = 0
media = 0
conceito = 0
if media in range(90, 100):
    media = 'A'
    notas = nota1, nota2
    media2 = media1
elif media in range(75, 90):
    media = 'B'
    notas = nota1, nota2
    media2 = media1
elif media in range(60, 75):
    media = 'C'
    notas = nota1, nota2
    media2 = media1
elif media in range(40, 60):
    media = 'D'
    notas = nota1, nota2
    media2 = media1
else:
    media = 'E'
    notas = nota1, nota2
    media2 = media1

print(f'Suas notas foram : {notas}')
print(f'Sua média foi    : {media2}')
print(f'Você tirou um    : {media}')

if media in ['A', 'B', 'C']:
    print('Você foi      : APROVADO')
else:
    print('Você foi      : REPROVADO')