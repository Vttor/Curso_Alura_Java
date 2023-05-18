def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero,"titular": titular,"saldo": saldo,"limite": limite}
    return conta

def deposita(conta,valor):
    conta["numero"] += valor

def saca(conta,valor):
    conta["numero"] -= valor

def extrato(conta):
    print("Seu saldo é de {}".format(conta["numero"]))

