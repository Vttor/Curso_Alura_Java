print("*********************************")
print("Bem vindo ao jogo da adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

print("Você digitou", chute_str, end="")

chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute < numero_secreto

if(acertou):
    print(" e acertou!")
elif(maior):
    print(" e errou! O seu chute foi menor que o número secreto.")
else:    
    print(" e errou! O seu chute foi maior que o número secreto.")

print("\nFim do Jogo!")

