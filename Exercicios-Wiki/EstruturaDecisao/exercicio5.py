#Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#1 A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#2 A mensagem "Reprovado", se a média for menor do que sete;
#3 A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota1 = float(input('Primeita nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1+nota2)/2
if media >= 100 :
    print('Aprovado com Distinção')
elif media >= 70 :
    print('Aprovado')
else:
    print('Reprovado')
