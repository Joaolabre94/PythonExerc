"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = 'Olha só que, coisa interessante'
lista_frases_cruas = frase.split(',')
print(frase)
print(lista_frases_cruas)
palavras = frase.split()
lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(frase)
print(lista_frases_cruas)
print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)

for i, frase in enumerate(lista_frases):
    print(lista_frases[i])

for i, palavra in enumerate(lista_frases_cruas):
    print(i, palavra)

bela = 'Me liga qualquer coisa. E amor, eu te amo muito <3'
bela_nova = bela.split('.')
print(bela_nova)
bela_nova2 = ' -'.join(bela_nova)
print(bela_nova2)