from descontos import DescontoNormal, DescontoVIP, DescontoPremium
from pedido import Pedido
from interfaces import IDesconto, ICupom

def aplicar_desconto(desconto: IDesconto, valor: float) -> float:
    return desconto.calcular(valor)

def aplicar_cupom(cupom: ICupom, codigo: str) -> bool:
    return cupom.aplicar_cupom(codigo)

if __name__ == "__main__":
    valor = 100.0

    # Testando via Inversão de Dependência (DIP) em Pedido
    pedido_normal = Pedido(DescontoNormal())
    pedido_vip = Pedido(DescontoVIP())

    print("Total Pedido Normal: R$", pedido_normal.total(valor))
    print("Total Pedido VIP: R$", pedido_vip.total(valor))

    # Testando Polimorfismo e Substituição de Liskov (LSP)
    print("Desconto Normal:", aplicar_desconto(DescontoNormal(), valor))
    print("Desconto VIP:", aplicar_desconto(DescontoVIP(), valor))
    print("Desconto Premium:", aplicar_desconto(DescontoPremium(), valor))

    # Testando Segregação de Interface (ISP)
    vip = DescontoVIP()
    print("Cupom VIP aplicado:", aplicar_cupom(vip, "DESC10"))
 