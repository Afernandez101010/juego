import personaje
class Compi(personaje):
    def __init__(self, compi, nivel, clase, hpCompi):
        super().__init__(nivel)
        self.compi = compi
        self.__hp = hpCompi

    @property
    def nivel(self):
        return super().__init__(self._nivel)
        
    nivel.setter
    def nivel(self, nuevo_nivel):
        self._nivel = nuevo_nivel