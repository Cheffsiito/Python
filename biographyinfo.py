def Nombre():
    while True:
        nombre = input("¿Cuál es tu nombre?: ")
        if nombre.strip():
            return nombre
        else:
            print("Por favor, ingresa un nombre válido.")

def Cumpleaños():
    while True:
        cumple = input("¿Cuál es tu fecha de nacimiento? (por ejemplo, Jan 1, 2000): ")
       
        if cumple.strip(): 
            return cumple
        else:
            print("Por favor, ingresa una fecha de nacimiento válida.")

def Direccion():
    while True:
        dire = input("¿Cuál es tu dirección?: ")
        if dire.strip(): 
            return dire
        else:
            print("Por favor, ingresa una dirección válida.")

def metas_personales():
    while True:
        metas = input("¿Cuáles son tus metas personales?: ")
        if metas.strip():  
            return metas
        else:
            print("Por favor, ingresa metas válidas.")

def main():
    print("Ingresa tus datos:")
    nombre = Nombre()
    cumple = Cumpleaños()
    dire = Direccion()
    metas = metas_personales()

   
    print("\nAqui estan tus datos")
    print("- Nombre:", nombre)
    print("- Fecha de nacimiento:", cumple)
    print("- Dirección:", dire)
    print("- Metas personales:", metas)

if __name__ == "__main__":
    main()
