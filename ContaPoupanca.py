from Conta import Conta
from tempo import ajustar_tempo


class ContaPoupanca(Conta):
    def __init__(self, id_conta: int, saldo: float, taxa_de_rendimento_ao_ano: float):
        super().__init__(id_conta, saldo)
        self.taxa_de_rendimento_ao_ano = taxa_de_rendimento_ao_ano

    def sacar(self, valor_a_ser_sacado: float):
        if valor_a_ser_sacado > self.get_saldo():
            raise ValueError(
                "O valor a ser sacadado é maior que o disponível.")
        else:
            self.set_saldo(self.get_saldo() - valor_a_ser_sacado)

    def depositar(self, valor_a_ser_depositado):
        self.set_saldo(self.get_saldo() + valor_a_ser_depositado)

    def calcular_rendimento(self, tempo_de_verificacao_do_rendimento: float, unidade_tempo: str):

        rendimento = self.get_saldo() * (1 + self.taxa_de_rendimento_ao_ano /
                                         100) ** ajustar_tempo(tempo=tempo_de_verificacao_do_rendimento, unidade_tempo=unidade_tempo)

        print(
            f"O rendimento de sua conta no prazo de {tempo_de_verificacao_do_rendimento} {unidade_tempo} é de: R${(rendimento - self.get_saldo())}")
