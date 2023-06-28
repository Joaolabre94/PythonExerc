"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
i = inicio, f = fim, p = passo(de quantos em quantos vai pular, padrao é 1)
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[::-1])
print(variavel[4::1])
print(len(variavel))
print(variavel[0:9:1])
print(variavel[-1:-10:-1])