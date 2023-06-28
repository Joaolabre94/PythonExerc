"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

def jogo ():
    tentativa = 0
    palavra_secreta = 'camilla'
    letras_acertadas = ''

    while True:
        tentativa = tentativa + 1
        palavra_formada = ''

        letra_digitada = input('Digite uma letra: ').lower()
        if len(letra_digitada) > 1:
            print('Digite apenas uma letra')
            continue

        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada +=  letra_secreta
            else:
                palavra_formada += '*'

        print(f'A palava formada é: {palavra_formada}')
        
        if palavra_secreta == palavra_formada:
            print(f'PARABÉNS! VOCÊ GANHOU! \nA palavra correta era Camilla! \nAs tentativas foram de: {tentativa}')
            break
    
jogo()