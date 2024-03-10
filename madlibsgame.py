def mad_libs():
    print("¡Bienvenido al juego de Mad Libs!")

    name = input("Ingresa un nombre: ")
    verb = input("Ingresa un verbo en presente: ")
    adjective = input("Ingresa un adjetivo: ")
    noun = input("Ingresa un sustantivo: ")

   
    story = f"Una vez, {name} {verb} en la playa {adjective}. De repente, vio un {noun} gigante."

   
    print("\nAquí está tu historia:\n")
    print(story)

if __name__ == "__main__":
    mad_libs()
