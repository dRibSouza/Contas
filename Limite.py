""" Para seguir melhor o princípio de responsabilidade única, o gerenciamento do limite da ContaCorrente poderia ser implementado em uma classe separada;
porém não consegui implementar efetivamente o funcionamento dos métodos da classe limite em ContaCorrente.
Da forma como está, o gerenciamento do limite também está sendo realizado pela classe ContaCorrente.
Abaixo segue o código de como acredito que poderia ser implementada a classe Limite, mesmo que eu não tenha conseguido aplicar na prática.

"""


class Limite:
    def __init__(self, limite_base: float):
        self.limite_base = limite_base
        self.limite_disponivel = self.limite_base

    def get_limite_base(self) -> float:
        return self.limite_base

    def set_limite_base(self, novo_limite: float):
        self.limite_base = novo_limite

    def get_limite_disponivel(self) -> float:
        return self.limite_disponivel

    def set_limite_disponivel(self, novo_limite_disponivel: float):
        self.limite_disponivel = novo_limite_disponivel
