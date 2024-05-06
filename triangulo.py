def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def generar_primos_hasta(numero):
    primos = []
    for i in range(2, numero + 1):
        if es_primo(i):
            primos.append(i)
    return primos

def main():
    altura = int(input("Por favor, ingresa la altura del triángulo (número entero): "))
    primos = generar_primos_hasta(altura)

    for i in range(len(primos)):
        for j in range(i + 1):
            print(primos[j], end=" ")
        print()

if __name__ == "__main__":
    main()
9