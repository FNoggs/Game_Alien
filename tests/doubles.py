from src.desconto.interfaces import IDesconto

class StubSemDesconto(IDesconto):
    """Stub que simula um cenário onde o desconto é sempre zero."""
    def calcular(self, valor):
        return 0