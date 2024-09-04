from client import Client
from account import Account

class main():
    pass

c1 = Client("João", "114444-2222")

account = Account(0, 0, c1._name)


account.extrato()
account.deposita(100)
account.extrato()
account.saque(100)
account.extrato()