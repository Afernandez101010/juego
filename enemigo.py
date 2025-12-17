
import personaje
class Enemigo(personaje):
    def __init__(self, raza, nivel, clase ):
        super().__init__(clase, nivel)
        self.raza = raza

    @property
    def nivel(self):
        return super().__init__(self.nivel)
        
    nivel.setter
    def nivel(self, nuevo_nivel):
        self._nivel = nuevo_nivel