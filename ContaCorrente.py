from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, id_conta: int, saldo: float, limite_base: float):
        super().__init__(id_conta, saldo)
        self.limite_base = limite_base
        self.limite_disponível = self.limite_base

    def sacar(self, valor_a_ser_sacado: float):
        if valor_a_ser_sacado > (self.limite_disponível + self.get_saldo()):
            raise ValueError(
                "O valor a ser sacadado é maior que o disponível.")
        elif valor_a_ser_sacado > self.get_saldo():
            self.limite_disponível -= (valor_a_ser_sacado - self.get_saldo())
            self.set_saldo(0)
        elif valor_a_ser_sacado > self.get_saldo():
            self.set_saldo(self.get_saldo() - valor_a_ser_sacado)

    def depositar(self, valor_a_ser_depositado):
        # Verifica se foi utilizado parte do limite para algum saque.
        #  Se algum saque tiver sido feito utilizando o limite, esse valor é reposto e o restante adicionado ao saldo.

        if self.limite_disponível <= self.limite_base and valor_a_ser_depositado <= self.limite_base - self.limite_disponível:
            self.limite_disponível += valor_a_ser_depositado
        elif self.limite_disponível <= self.limite_base and valor_a_ser_depositado > self.limite_base - self.limite_disponível:
            self.set_saldo += valor_a_ser_depositado - \
                (self.limite_base - self.limite_disponível)
            self.limite_disponível = self.limite_base
        else:
            self.set_saldo += valor_a_ser_depositado
