def es_palindromo(palabra):
    palabra = palabra.lower()
    palabra_sin_espacios = palabra.replace(" ", "")
    return palabra_sin_espacios == palabra_sin_espacios[::-1]

def main():
    palabra = input("Por favor, ingresa una palabra: ")
    if es_palindromo(palabra):
        print("La palabra es un palíndromo.")
    else:
        print("La palabra no es un palíndromo.")

if __name__ == "__main__":
    main()
