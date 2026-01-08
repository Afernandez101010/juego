from guerrero import Guerrero
from mago import Mago
from orco import Orco
from compi import Compi

def mostrar_menu():
    print("\n--- MENÚ RPG ---")
    print("1. Crear personaje")
    print("2. Iniciar combate")
    print("3. Salir")

jugador = None
compi = Compi("Aliado")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre de tu personaje: ")
        clase = input("Clase (guerrero/mago): ").lower()
        if clase == "guerrero":
            jugador = Guerrero(nombre)
        elif clase == "mago":
            jugador = Mago(nombre)
        else:
            print("Clase incorrecta")
            continue
        print(f"{jugador.nombre} creado con éxito.")

    elif opcion == "2":
        if not jugador:
            print("Primero crea un personaje")
            continue

        enemigo = Orco()
        print("\n¡Comienza el combate!")

        while jugador.ver_hp() > 0 and enemigo.ver_hp() > 0:
            input("\nEnter para siguiente turno…")
            jugador.atacar(enemigo)
            if enemigo.ver_hp() <= 0:
                print("Enemigo derrotado")
                jugador.subir_nivel()
                break

            input("\nEnter para siguiente turno…")
            compi.atacar(enemigo)
            if enemigo.ver_hp() <= 0:
                print("Enemigo derrotado")
                jugador.subir_nivel()
                break

            input("\nEnter para siguiente turno…")
            enemigo.atacar(jugador)
            if jugador.ver_hp() <= 0:
                print("Has sido derrotado")
                break

            print(f"\nHP actuales: {jugador.nombre}: {jugador.ver_hp()} | {compi.nombre}: {compi.ver_hp()} | {enemigo.nombre}: {enemigo.ver_hp()}")

    elif opcion == "3":
        print("Saliendo del juego…")
        break

    else:
        print("Opción no válida")
