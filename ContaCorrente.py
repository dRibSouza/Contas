from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, id_conta: int, saldo: float, limite: float):
        super().__init__(id_conta, saldo)
        self.limite = limite

    def sacar(self, valor_a_ser_sacado: float):
        if valor_a_ser_sacado > (self.limite + self.get_saldo()):
            raise ValueError(
                "O valor a ser sacadado é maior que o disponível.")
        elif valor_a_ser_sacado > self.get_saldo():
            self.limite = self.limite - (valor_a_ser_sacado - self.get_saldo())
            self.set_saldo(0)
        elif valor_a_ser_sacado > self.get_saldo():
            self.set_saldo(self.get_saldo() - valor_a_ser_sacado)

    def depositar(self):
        return super().depositar()


conta = ContaCorrente(1, 100, 50)

conta.sacar(valor_a_ser_sacado=160)

print("Saldo atual: ", conta.get_saldo())

print("Limite atual: ", conta.limite)
