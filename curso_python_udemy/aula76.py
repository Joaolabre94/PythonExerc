"""
Faça um jogo para o usuário adivinhar qual a palavra secreta
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra certa.
- Se a letra digitada estiver na palavra certa; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiva *.
- Faça a contagem de tentativas do seu usuário"""

def jogo():
    palavra_secreta = 'sexo'
    palavra_atual = ['*'] * len(palavra_secreta)
    tentativas = 0

    while '*' in palavra_atual:
        tentativas = tentativas + 1
        letra = input('Digite uma letra: ').lower()
        if len(letra) != 1:
            print('Digite apenas uma letra')
            continue
        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    palavra_atual[i] = letra
        else:
            print(" ", end='')

        print(f"Palavra atual: ", " ".join(palavra_atual))

    print(f"Parabéns! Você adivinhou a palavra secreta '{palavra_atual}' em", tentativas, "tentativas.")

jogo()

