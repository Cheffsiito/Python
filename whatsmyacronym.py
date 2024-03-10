def Acronimo(phrase):
   
    words = phrase.split()
    acronimo = ""

    for word in words:
        acronimo += word[0].upper()

    return acronimo

def main():
    
    full_meaning = input("Ingresa el concepto ")

   
    acronimo = Acronimo(full_meaning)


    print("El acrónimo para '{}' es: {}".format(full_meaning, acronimo))

if __name__ == "__main__":
    main()
