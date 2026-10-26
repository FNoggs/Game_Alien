from abc import ABC, abstractmethod

class IDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass

class ICupom(ABC):
    @abstractmethod
    def aplicar_cupom(self, codigo: str) -> bool:
        pass

class IVIP(ABC):
    @abstractmethod
    def validar_usuario_vip(self, usuario: str) -> bool:
        pass