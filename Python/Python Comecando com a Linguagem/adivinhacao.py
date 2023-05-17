import random

print("*********************************")
print("Bem vindo ao jogo da adivinhação!")
print("*********************************")

pontos = 1000
numero_secreto = random.randrange(1,101)
#rodada = 1

print("Escolha a dificuldade do jogo")
print("(1) Fácil  (2) Médio  (3) Difícil")
nivel = int(input("Dificuldade: " ))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
elif(nivel == 3):
    total_de_tentativas = 5


#while(rodada <= total_de_tentativas):
for rodada in range (1,total_de_tentativas+1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número entre 1 e 100: ")
    chute = int(chute_str)

    chute_invalido = chute < 1 or chute > 100
    if(chute_invalido):
        print("Você deve chutar um numero entre 1 e 100.")
        continue

    print("Você digitou", chute_str, end="")

    acertou = chute == numero_secreto
    maior = chute < numero_secreto


    if(acertou):
        print(" e acertou! Você fez {} pontos",format(pontos))
        break
    elif(maior):
        print(" e errou! O seu chute foi menor que o número secreto.")
    else:    
        print(" e errou! O seu chute foi maior que o número secreto.")
    pontos_perdidos = abs(numero_secreto-chute)
    pontos = pontos - pontos_perdidos

print("\nFim do Jogo!")

