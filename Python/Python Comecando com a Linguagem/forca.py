import random

def exibir_mensagem_de_inicio():
    print("*********************************")
    print("Bem vindo ao jogo de forca!")
    print("*********************************")

def escolher_palavra_secreta():
    arquivo = open("palavras.txt","r")
    palavras = [linha.strip().upper() for linha in arquivo]
    arquivo.close()

    return( palavras[random.randrange(0,len(palavras))] )

def iniciar_letras_acertadas(palavra_secreta):
    return (["_" for letra in palavra_secreta])

def confere_chute(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = chute
        index+=1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
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

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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

    if(erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

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

    if (erros >= 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def iniciar():

    exibir_mensagem_de_inicio()

    palavra_secreta = escolher_palavra_secreta()

    letras_acertadas = iniciar_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    desenha_forca(erros)
    print(letras_acertadas)
    while(not enforcou and not acertou):
        
        chute = input("Letra: ").upper().strip()
        if(chute in palavra_secreta):
            confere_chute(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 8
        acertou = "_" not in letras_acertadas
        
        desenha_forca(erros)
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()

    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("\nFim do Jogo!")

if(__name__ == "__main__"):
    iniciar()