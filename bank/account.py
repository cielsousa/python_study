
class Account():
    def __init__(self, saldo, number, titularity) -> None:
        self._saldo = saldo
        self.number = number
        self.titularity = titularity


    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if (saldo <0):
            print("Saldo can't be negative")

        else:
            self._saldo = saldo

    def saque(self, valor):
        if(self.saldo>=valor):
            self.saldo-=valor
            print("Saque realizado com sucesso")

        else:
            print("Saldo insuficiente")

    def deposita(self, valor):
        self.saldo += valor

    def extrato(self):
        print('Olá seu saldo é de:', self.saldo)