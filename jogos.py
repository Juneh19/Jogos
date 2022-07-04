import adivinhacao
import forca

print("********************************")
print("***Bem vinde! Escolha o jogo!***")
print("********************************")
print("(1) Adivinhação, (2) Forca")
jogo = int(input("Defina o seu jogo: "))

if jogo == 1:
    print("Jogando adivinhção.")
    adivinhacao.jogar()
elif jogo == 2:
    print("Jogando forca.")
    forca.jogar()
