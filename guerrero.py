from personaje import Personaje

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, hp=100, daño=12)

    def atacar(self, objetivo):
        if self._cooldown >= 2:
            usar = input(f"{self.nombre}: ¿Usar habilidad especial? (s/n): ").lower()
            while usar not in ("s","n"):
                usar = input("Por favor ingresa 's' o 'n': ").lower()
            if usar == "s":
                self.usar_habilidad(objetivo)
                self._cooldown = 0
                return
            elif usar == "n":
                objetivo.recibir_daño(self._Personaje__daño)
        else:
            self._cooldown += 1
            objetivo.recibir_daño(self._Personaje__daño)
        print(f"{self.nombre} ataca con espada y hace {self._Personaje__daño} de daño")

    def usar_habilidad(self, objetivo):
        daño = self._Personaje__daño + 5
        objetivo.recibir_daño(daño)
        print(f"{self.nombre} usa Golpe Poderoso y hace {daño} de daño")
