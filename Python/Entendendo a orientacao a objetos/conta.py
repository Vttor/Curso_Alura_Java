
from typing import Any


class Conta:
    
    def __init__(self,numero: int, titular: str, saldo: float, limite: float) -> None:
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo,self.__titular))

    def __pode_sacar(self,valor):
        valor_disponivel_para_sacar = self.__saldo + self.__limite
        return valor <= valor_disponivel_para_sacar

    def saca(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))
    
    def deposita(self,valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    @property
    def numero(self):
        return self.__numero
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, valor):
        self.__limite = valor
    @property
    def titular(self):
        return self.__titular
    @staticmethod
    def codigo_banco():
        return "001"
    