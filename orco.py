from enemigo import Enemigo

class Orco(Enemigo):
    def __init__(self):
        super().__init__("Orco", hp=80, daño=12)

    def usar_habilidad(self, objetivo):
        daño = 20
        objetivo.recibir_daño(daño)
        print(f"{self.nombre} usa Ataque Salvaje y hace {daño} de daño")
