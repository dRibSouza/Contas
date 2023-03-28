from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, id_conta: int, saldo: float, limite_base: float):
        super().__init__(id_conta, saldo)
        self.limite_base = limite_base
        self.limite_disponivel = self.limite_base

    def sacar(self, valor_a_ser_sacado: float):
        # O valor do saldo para saque é o valor do limite disponível mais o saldo, caso essa verificação não seja verdadeira um erro é informado
        if valor_a_ser_sacado > (self.limite_disponivel + self.get_saldo()):
            raise ValueError(
                "O valor a ser sacadado é maior que o disponível.")
        # Caso em que será necessário utilização do limite para realizar um saque
        elif valor_a_ser_sacado > self.get_saldo():
            self.limite_disponivel -= (valor_a_ser_sacado - self.get_saldo())
            self.set_saldo(0)
        # Caso em que o saldo é suficiente para realizar o saque. 
        elif valor_a_ser_sacado > self.get_saldo():
            self.set_saldo(self.get_saldo() - valor_a_ser_sacado)

    def depositar(self, valor_a_ser_depositado):
        # Verifica se foi utilizado parte do limite para algum saque.
        # Se algum saque tiver sido feito utilizando o limite, esse valor é reposto e o restante do depósito é adicionado ao saldo.
        
        # Esse caso representa o deposito referente a um valor que será utilizado para restituição do limite porém não é suficiente para adicionar ao saldo
        if self.limite_disponivel <= self.limite_base and valor_a_ser_depositado <= self.limite_base - self.limite_disponivel:
            self.limite_disponivel += valor_a_ser_depositado
            
        # deposito de um valor maior que o limite a ser reposto de forma que o excedente é adicionado ao saldo
        elif self.limite_disponivel <= self.limite_base and valor_a_ser_depositado > self.limite_base - self.limite_disponivel:
            self.set_saldo += valor_a_ser_depositado - (self.limite_base - self.limite_disponivel)
            self.limite_disponivel = self.limite_base
            
        # caso em que o limite não foi utilizado para um saque anterior
        else:
            self.set_saldo += valor_a_ser_depositado
