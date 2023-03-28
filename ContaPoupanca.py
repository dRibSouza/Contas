from Conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, id_conta: int, saldo: float, taxa_de_rendimento_ao_ano: float):
        super().__init__(id_conta, saldo)
        self.taxa_de_rendimento_ao_ano = taxa_de_rendimento_ao_ano

    def sacar(self):
        return super().sacar()

    def depositar(self):
        return super().depositar()
