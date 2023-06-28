#Faça um Programa que peça a temperatura em graus Fahrenheit, 
#transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
fahre = float(input('Qual o valor em Fahrenheit: '))
c = 5 * ((fahre-32) / 9)
print(f'A temperatura em graus Celsius é de: {c}')