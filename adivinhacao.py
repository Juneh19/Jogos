import random


def jogar():
    print("********************************")
    print("Bem vinde ao jogo de adivinhação!")
    print("********************************")
    print("Niveis 1, 2 e 3.")
    nivel = int(input("Defina a dificuldade: "))

    if nivel == 1:
        tentativas = 15
    elif nivel == 2:
        tentativas = 10
    else:
        tentativas = 5

    senha = random.randrange(1, 101)

    while tentativas > 0:
        print("Tentativas restantes: {}.". format(tentativas))
        chute = input("Digite o seu número: ")
        numero = int(chute)
        print("Você digitou {}.". format(numero))
        if numero < 1 or numero > 100:
            print("Você deve digitar um número entre 1 e 100.")
            continue
        if numero == senha:
            print("Acerto miseravi.")
            tentativas = 0
        else:
            if numero < senha:
                print("Erroooou! Você chutou um número menor.")
            elif numero > senha:
                print("Erroooou! Você chutou um número maior.")
            tentativas = tentativas - 1

    print("Fim de jogo.")
    print("O número era {}".format(senha))


if __name__ == "__main__":
    jogar()
