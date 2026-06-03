class Conta:
    def __init__(self,numeroConta,cliente,extrato = None,saldo = 0):
        self.numeroConta = numeroConta
        self.saldo = saldo
        self.extrato = extrato if extrato is not None else []
        self.cliente = cliente