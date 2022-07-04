import random


def apresentacao():
    print("********************************")
    print("***Bem vinde ao jogo de forca!***")
    print("********************************")


def palavra():
    lista = open("palavrasFaceis.txt", "r")
    palavras = []
    for linha in lista:
        linha = linha.strip()
        palavras.append(linha)
    lista.close()
    numero = random.randrange(0, len(palavras))
    senha = palavras[numero].upper()
    return senha


def chutar():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute


def chute_certo(senha, chute, letras_acertadas):
    index = 0
    for letra in senha:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def mensagem_vitoria():
    print("Você ganhou XD.")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mensagem_derrota(senha):
    print("Vish, você perdeu ;-;.")
    print("A palavra era {}".format(senha))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")


def jogar():

    apresentacao()
    senha = palavra()
    letras_acertadas = ["_" for letra in senha]

    enforcado = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while not enforcado and not acertou:
        chute = chutar()

        if chute in senha:
            chute_certo(senha, chute, letras_acertadas)
        else:
            erros += 1
            print(desenha_forca(erros))
        enforcado = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        mensagem_vitoria()
    else:
        mensagem_derrota(senha)
    print("Fim de jogo.")


if __name__ == "__main__":
    jogar()
