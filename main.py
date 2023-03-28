from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# TESTES PARA CONTA CORRENTE

minha_conta_corrente = ContaCorrente(1, 100, 50)
# Métodos de ContaCorrente
# sacar(valor_a_ser_sacado:float)
# depositar(valor_a_ser_depositado:float)

# Sacando um valor além do permitido um erro do tipo ValueError é informado
# minha_conta_corrente.sacar(valor_a_ser_sacado=160)


print("Saldo: ", minha_conta_corrente.get_saldo())
print("Limite disponível: ", minha_conta_corrente.limite_disponivel)

minha_conta_corrente.sacar(valor_a_ser_sacado=120)

print("Saldo após saque de 120: ", minha_conta_corrente.get_saldo())

print("Limite disponível após saque de 120: ",
      minha_conta_corrente.limite_disponivel)

minha_conta_corrente.depositar(15)

print("Saldo após depósito de 15: ", minha_conta_corrente.get_saldo())
print("Limite disponível após depósito de 15: ",
      minha_conta_corrente.limite_disponivel)

# TESTES PARA CONTA POUPANÇA

# Métodos de ContaCorrente
# sacar(valor_a_ser_sacado:float)
# depositar(valor_a_ser_depositado:float)
# calcular_rendimento(tempo_de_verificacao_do_rendimento:float, unidade_tempo:str)

minha_conta_poupanca = ContaPoupanca(1, 1000, 8.3)

print("Saldo: ", minha_conta_poupanca.get_saldo())


minha_conta_poupanca.sacar(150)
print("Saldo após saque de 150: ", minha_conta_poupanca.get_saldo())

minha_conta_poupanca.depositar(1000)

print("Saldo após depósito de 1000: ", minha_conta_poupanca.get_saldo())

minha_conta_poupanca.calcular_rendimento(1.5, "anos")

minha_conta_poupanca.calcular_rendimento(18, "meses")
