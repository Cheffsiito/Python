def main():
    while True:
        try:
            number = int(input("¡Hola! ¿Qué número estás pensando entre 1 y 1000?: "))
            if 1 <= number <= 1000:
                if number % 2 == 0:
                    print("¡Ese es un número par!")
                else:
                    print("¡Ese es un número impar!")
            else:
                print("Por favor, introduce un número entre 1 y 1000.")
        except ValueError:
            print("Por favor, introduce un número válido.")

        choice = input("¿Quieres intentarlo de nuevo? (s/n): ")
        if choice.lower() != 's':
            break

if __name__ == "__main__":
    main()
