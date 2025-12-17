from abc import ABC, abstractmethod
class Personaje:
    @abstractmethod
    def __init__(self, nivel, clase, nombre = ""):
        self.nombre = nombre
        self._nivel = nivel
        self.__clase = clase

    @property
    def nivel(self):
        return self._nivel
        
    nivel.setter
    def nivel(self, nuevo_nivel):
        self._nivel = nuevo_nivel