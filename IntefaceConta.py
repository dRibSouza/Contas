# Essa classe foi criada para garantir o princípio de única responsabildiade, implementando a interface das contas bancárias, liberando a classe Conta para realizar o acesso e
# manutenção do estado dos atributos saldo e id_conta
from abc import ABC, abstractmethod


class InterfaceConta(ABC):
    @abstractmethod
    def depositar(self, valor: float):
        pass

    @abstractmethod
    def sacar(self, valor: float):
        pass
