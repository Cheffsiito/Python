from random import randint
 
choice = ["piedra","papel","tijeras"]
def main():
    computer = choice[randint(0,2)]
 
    print("Bienvenido a piedra papel y tijeras\n")
    player = input("Elige: ").lower()
    print("La computadora eligio: " + computer)
 
    if player == computer:
        print("Empate")
    elif player == "piedra" and computer == "papel":
        print("Gano la Computadora")
    elif player == "piedra" and computer == "tijeras":
        print("Gano el jugador")
    elif player == "papel" and computer == "piedra":
        print("Gano el jugador")
    elif player == "papel" and computer == "tijeras":
        print("Gano la Computadora")
    elif player == "tijeras" and computer  == "piedra":
        print("Gano la Computadora")
    elif player == "tijeras" and computer == "papel":
        print("Gano el jugador")
    elif player == "end":
        StopIteration
 
    main()
 
main()