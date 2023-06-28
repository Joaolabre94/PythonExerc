seq = [0, 1, 2]
print(seq)
#Usar [0:4] provoca a impressão dos índices 0, 1, 2 e 3, mas não do índice 4.
#  Analogamente, usar [2:8] provoca a impressão dos índices de 2 a 7, 
# mas não do 8.
str = 'Hello World'
print(str[0:4])
print(str[2:8])
#Também é possível imprimir a string como lida da direita para a esquerda. 
# Para isso, deve-se utilizar [: : -1]. 
# Esse valor -1 indica que a leitura dos caracteres será feita no sentido 
# oposto ao tradicional.
print(str[::-1])
print(str[8:2:-1])