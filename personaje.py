from abc import ABC, abstractmethod
from habilidades import Habilidades

class Personaje(Habilidades, ABC):
    def __init__(self, nombre="", hp=100, daño=0):
        self.nombre = nombre           # público: se muestra en el menú
        self._nivel = 1                # protegido: accesible por hijas
        self.__hp = hp                 # privado: control interno de la clase
        self.__daño = daño             # privado: control del daño base
        self._cooldown = 2             # protegido: para la lógica de ataques especiales

    def recibir_daño(self, daño):
        self.__hp -= daño
        if self.__hp < 0:
            self.__hp = 0

    def ver_hp(self):
        return self.__hp

    def subir_nivel(self):
        self._nivel += 1
        self.__daño += 1
        self.__hp = 100
        print(f"{self.nombre} ha subido a nivel {self._nivel}")
        print(f"El daño ahora es {self.__daño}")
        print(f"HP restaurado a {self.__hp}%")
