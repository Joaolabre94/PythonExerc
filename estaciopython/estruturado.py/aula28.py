#Implementar uma solução em python que faça o tratamento de exceção para verificar se uma entrada é numérica e que,
#além disso, insista que o usuário digite um Número válido.
while True:
    def valor():
        try:
            x = int(input('Digite um valor: '))
            break
        except ValueError:
             print('Valor incorreto, entre com valor certo!')
    
