# 4) Escreva um programa que receba três valores ponto flutuante de precisão dupla (a, b, 
# c) e responda se a soma “a+b” é igual a “c”. Teste com a = 0,1 , b = 0,2 e c = 0,3.
import math
def calculo(a, b, c):
        resultado = (a) + (b)
        if math.isclose(resultado, c):
            return resultado
        

    
def valores():
    while True:
        try:
            a = float(input('Digite uma fração: '))
            b = float(input('Digite uma segunda fração: '))
            c = float(input('Digite uma segunda fração: '))
            if calculo(a,b,c):
                resultado = calculo(a,b,c)
                print(f'A soma dos números foi: {resultado:.2f}')
                break
            else:
                print(f'A soma dos numeros {a} + {b} não foi igual a {c}')
                break
        except:
            print('Digite um número correto.')

valores()