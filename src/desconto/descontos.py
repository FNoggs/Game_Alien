from src.desconto.interfaces import IDesconto, ICupom, IVIP

class DescontoNormal(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1

class DescontoVIP(IDesconto, ICupom, IVIP):
    def calcular(self, valor: float) -> float:
        return valor * 0.2

    def aplicar_cupom(self, codigo: str) -> bool:
        return codigo == "DESC10"

    def validar_usuario_vip(self, usuario: str) -> bool:
        return usuario == "vip"

class DescontoPremium(IDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.3