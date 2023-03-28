from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# TESTES PARA CONTA CORRENTE

minha_conta_corrente = ContaCorrente(1, 100, 50)

minha_conta_corrente.sacar(valor_a_ser_sacado=120)

print("Saldo: ", minha_conta_corrente.get_saldo())

print("Limite disponível: ", minha_conta_corrente.limite_disponível)

minha_conta_corrente.depositar(15)

print("Saldo: ", minha_conta_corrente.get_saldo())
print("Limite disponível: ", minha_conta_corrente.limite_disponível)

# TESTES PARA CONTA POUPANÇA

minhaContaPoupanca = ContaPoupanca(1, 1000, 8.3)
minhaContaPoupanca.sacar(150)

minhaContaPoupanca.calcular_rendimento(1.5, "anos")
minhaContaPoupanca.calcular_rendimento(18, "meses")
