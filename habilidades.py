from abc import ABC, abstractmethod
class Habilidades(ABC):

    @abstractmethod
    def atacar(self, objetivo):
        pass

    @abstractmethod
    def usar_habilidad(self, objetivo):
        pass

    @abstractmethod
    def recibir_daño(self, daño):
        pass

    @abstractmethod
    def ver_hp(self):
        pass
