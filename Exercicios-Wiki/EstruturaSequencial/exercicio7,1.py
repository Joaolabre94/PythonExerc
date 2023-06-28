#Faça um Programa que calcule a área de um quadrado, 
#em seguida mostre o dobro desta área para o usuário.
def valores():
    while True:
        try:
            altura = float(input('Digite um dos lados do quadrado: '))
            x = (altura**2) 
            dobro = x * 2
            print(f'A área do quadrado é: {x:.2f}, e o dobro da área é: {dobro:.2f}')
            break
        except:
            print(f'Por favor, digite um dos lados corretamente.')
valores()