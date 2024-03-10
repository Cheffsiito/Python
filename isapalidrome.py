def obtener_entrada():
    entrada_bruta = input("\nPor favor, ingresa una palabra, frase u oración \npara verificar si es un palíndromo: ") 
    cadena_minusculas = entrada_bruta.lower() 
    lista_entrada = list(cadena_minusculas) 
    return lista_entrada

def quitar_no_alfabeticos(lista_no_limpia): 
    caracteres_no_alfabeticos = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
    for caracter in caracteres_no_alfabeticos: 
        if caracter in lista_no_limpia: 
            lista_no_limpia.remove(caracter) 
            return quitar_no_alfabeticos(lista_no_limpia)
    return lista_no_limpia 

def ejecutar_verificacion_palindromo(lista_original):
    lista_invertida = lista_original[::-1] 
    if lista_invertida == lista_original: 
        return "¡El texto que has ingresado es un palíndromo!" 
    else: 
        return "El texto que has ingresado no es un palíndromo." 

def main(): 
    print("\nVerificador de palíndromos") 
    lista_original = obtener_entrada()  
    lista_original = quitar_no_alfabeticos(lista_original) 
    resultado_palindromo = ejecutar_verificacion_palindromo(lista_original)
    print(resultado_palindromo)

if __name__ == "__main__":
    main()
