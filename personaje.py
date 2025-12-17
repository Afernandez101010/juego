from abc import ABC, abstractmethod
class Personaje:
    @abstractmethod
    def __init__(self,  Vida= 100, nombre = "", nivel= 1, clase= "", daño= 0):
        self.nombre = nombre
        self._nivel = nivel
        self.__clase = clase
        self.__hp = Vida
        self.__daño = daño

    @property
    def nivel(self):
        return self._nivel
        
    nivel.setter
    def nivel(self, nuevo_nivel):
        self._nivel = nuevo_nivel

    def crear_pj(self):
        nombre=input("Dime el nombre: ")
        self.nombre = nombre
        print("Clases: Guerrero / Mago")
        clase=input("Dime la clase: ").lower()
        if clase == "guerrero" or clase == "mago":
            self.__clase = clase
        else:
            print("Esa clase no es correcta")

    def atacar(self):
        if self.__clase == "guerrero":
            self.__daño = 12
            
        else:
            print("No has creado un personaje. ")