from personaje import Personaje
def menu():
    print("---------RPG VENEZOLANO---------")     
    while True:   
        print("---------Menu---------")     
        print("1.Crear personaje")
        print("2.Atacar")
        print("3.Salir")
        print("----------------------")
        elige = int(input("Elige una opcion: "))
        
        match elige:
            case 1:
                pass
            
            case 2:
                pass      
            
            case _:
                break

if __name__ == "__main__":
    menu()