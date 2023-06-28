# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem

def valores():
    while True:
        try:
            base = int(input('Digite o valor da base: '))
            expoente = int(input('Digite o valor do expoente: '))
            resultado = base ** expoente
            print(f'{base} elevado a {expoente} é: {resultado:.2f}')
            break       
            

        except:
            print('Digite valores corretos.')


valores()

