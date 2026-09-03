from normal import DescontoNormal
from vip import DescontoVip
from premium import DescontoPremium
from absdesc import Desconto

def aplicar_desconto(desconto: Desconto, valor:float):
    return desconto.calcular(valor)

def main():

    valor = 1000
    desconto_normal = DescontoNormal()
    desconto_vip = DescontoVip()
    desconto_premium = DescontoPremium()

    print(f"Desconto Normal: {aplicar_desconto(desconto_normal, valor):.2f}")
    print(f"Desconto Vip: {aplicar_desconto(desconto_vip, valor):.2f}")
    print(f"Desconto Premium: {aplicar_desconto(desconto_premium, valor):.2f}")

if __name__ == "__main__":
    main() 

