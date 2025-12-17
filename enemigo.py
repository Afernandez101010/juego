
import personaje
class Enemigo(personaje):
    def __init__(self, nivel , hp= 10, daño=10, raza= "orco"):
        super().__init__(nivel)
        self.raza = raza
        self.__hp= hp
        self.__daño = daño

    @property
    def nivel(self):
        return super().__init__(self.nivel)
        
    nivel.setter
    def nivel(self, nuevo_nivel):
        self._nivel = nuevo_nivel

