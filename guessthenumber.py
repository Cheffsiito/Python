import random

numero = random.randrange(1,50)
guess = int(input("Escribe un numero entre el 1 y el 50: "))

while guess != numero:
    if guess < numero:
        print("Eligue algo mas arriba")
        guess = int(input("Escribe un numero entre el 1 y el 50: "))
    else:
         print("Eligue algo mas abajo")
         guess = int(input("Escribe un numero entre el 1 y el 50: "))
print("Adivinaste!")