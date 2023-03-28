from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, id_conta: int, saldo: float):
        self._id_conta = id_conta
        self._saldo = saldo

    @abstractmethod
    def depositar(self):
        pass

    @abstractmethod
    def sacar(self):
        pass

    def get_id_conta(self):
        return self._id_conta

    def set_text(self, valor):
        self._id_conta = valor

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, valor: float):
        self._saldo = valor
