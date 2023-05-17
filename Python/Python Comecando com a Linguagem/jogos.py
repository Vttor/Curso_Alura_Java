import forca
import adivinhacao


print("*********************************")
print("Escolha o seu jogo:")
print("*********************************")

print("\n (1) Forca (2) Adivinhação")

jogo = int(input("Jogo: "))

if(jogo == 1):
    forca.iniciar()
elif(jogo == 2):
    adivinhacao.iniciar()