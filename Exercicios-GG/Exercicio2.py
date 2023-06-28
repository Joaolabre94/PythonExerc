#Suponha que um caixa automático disponha paneas de notas de 1, 10 e 50 reais.
#Considerando que alguém está fazendo um saque, implemente um programa que mostre o número
#mínimo de notas que o caixa deve entregar ao cliente. Exemplo:
#Qual o valor do saque? 72
#Você receberá 1 nota(s) de R$50,00
#2 nota(s) de R$10,00
#2 nota(s) de R$1,00
def valores():
    while True:
        try:
            saque = int(input('Registre a quantidade desejada: '))

            notas50 = saque // 50
            resto = saque % 50

            notas10 = resto // 10
            resto = resto % 10

            notas1 = resto

            print("Você receberá:")
            print(notas50, "nota(s) de R$ 50,00")
            print(notas10, "nota(s) de R$ 10,00")
            print(notas1, "nota(s) de R$ 1,00")
            break
        except:
            print('Digite o valor correto.')
valores()