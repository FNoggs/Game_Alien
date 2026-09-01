from normal import DescontoNormal
from vip import DescontoVip
from premium import DescontoPremium

def main():

    valor = 1000
    desconto_normal = DescontoNormal()
    desconto_vip = DescontoVip()
    desconto_premium = DescontoPremium()

    print(f"Desconto Normal: {desconto_normal.calcular(valor):.2f}")
    print(f"Desconto : {desconto_vip.calcular(valor):.2f}")
    print(f"Desconto Premium: {desconto_premium.calcular(valor):.2f}")

if __name__ == "__main__":
    main() 

