# Tuplas en Python


Una tupla en Python es una estructura de datos similar a una lista, pero a diferencia de las listas, las tuplas son inmutables, es decir, una vez creada una tupla, no se puede modificar. Las tuplas se utilizan comúnmente para almacenar colecciones de elementos relacionados que no deben cambiar, como coordenadas, nombres y valores constantes.

También se pueden crear tuplas sin paréntesis, simplemente separando los elementos por comas. Por ejemplo:


```
mi_tupla = 1, 2, 3, 4, 5
```

Los elementos de una tupla se pueden acceder utilizando índices, al igual que en las listas. Por ejemplo:
```
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla[0])  # Output: 1
```

>Las tuplas son inmutables, lo que significa 
que no se pueden modificar después de su creación. 
Las listas, por otro lado, son mutables.
Dado que las tuplas son inmutables, no admiten 
operaciones que cambien sus elementos, como agregar, 
eliminar o modificar elementos.
Sin embargo, puedes "eliminar" una tupla eliminando la referencia a la misma, es decir, asignando None a la variable que la contiene. Esto no elimina la tupla en sí, pero libera la memoria asociada a ella al permitir que el recolector de basura de Python la elimine de la memoria cuando ya no esté en uso. 

Aquí tienes un ejemplo:
```
mi_tupla = (1, 2, 3)
mi_tupla = None  # Elimina la referencia a la tupla
```

Las tuplas se pueden concatenar utilizando el operador +. Por ejemplo:
```
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Output: (1, 2, 3, 4, 5, 6)
```

Una tupla se puede repetir utilizando el operador *. Por ejemplo:
```
tupla_original = (1, 2)
tupla_repetida = tupla_original * 3
print(tupla_repetida)  # Output: (1, 2, 1, 2, 1, 2)
```
# Métodos de las Tuplas
count(): Devuelve el número de veces que aparece un elemento en la tupla.

index(): Devuelve el índice de la primera aparición de un elemento en la tupla.

# Ejercicios
**1-** Crea una tupla llamada mi_tupla con elementos del 1 al 5.

**2-** Accede al tercer elemento de la tupla mi_tupla.

**3-** Concatena dos tuplas y guarda el resultado en una nueva variable.

**4-** Repite una tupla tres veces y guarda el resultado en una nueva variable.

**5-** Escribe una función que tome una tupla como argumento y devuelva la suma de todos los elementos.

**6-** Escribe una función que tome una tupla como argumento y devuelva una nueva tupla con solo los elementos únicos.

**7-** Escribe una función que tome dos tuplas como argumentos y devuelva una nueva tupla que contenga solo los elementos que aparecen en ambas tuplas.

**8-** Escribe una función que tome una lista de tuplas como argumento y devuelva una nueva tupla que contenga el elemento más grande de cada tupla.

**9-** Escribe una función que tome una lista de números como argumento y devuelva una tupla con el número más grande y el número más pequeño.

**10-** Escribe una función que tome una tupla de cadenas como argumento y devuelva una nueva tupla donde cada cadena tenga la primera letra en mayúscula.



**1-**
```
mi_tupla = (1, 2, 3, 4, 5)
```
**2-**
```
tercer_elemento = mi_tupla[2]
print(tercer_elemento)  # Output: 3
```
**3-**
```
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Output: (1, 2, 3, 4, 5, 6)
```
**4-**
```
tupla_original = (1, 2, 3)
tupla_repetida = tupla_original * 3
print(tupla_repetida)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
```
**5-**
```
def suma_tupla(tupla):
    return sum(tupla)

# Ejemplo de uso:
mi_tupla = (1, 2, 3, 4, 5)
resultado = suma_tupla(mi_tupla)
print(resultado)  # Output: 15
```
**6-**
```
def elementos_unicos(tupla):
    return tuple(set(tupla))

# Ejemplo de uso:
mi_tupla = (1, 2, 2, 3, 3, 4, 5)
resultado = elementos_unicos(mi_tupla)
print(resultado)  # Output: (1, 2, 3, 4, 5)
```
**7-**
```
def elementos_comunes(tupla1, tupla2):
    return tuple(set(tupla1) & set(tupla2))

# Ejemplo de uso:
tupla1 = (1, 2, 3, 4)
tupla2 = (3, 4, 5, 6)
resultado = elementos_comunes(tupla1, tupla2)
print(resultado)  # Output: (3, 4)
```
**8-**
```
def elementos_mas_grandes(lista_de_tuplas):
    return tuple(max(tupla) for tupla in lista_de_tuplas)

# Ejemplo de uso:
lista_de_tuplas = [(1, 2), (4, 5), (7, 8)]
resultado = elementos_mas_grandes(lista_de_tuplas)
print(resultado)  # Output: (2, 5, 8)
```
**9-**
```
def extremos(lista):
    return min(lista), max(lista)

# Ejemplo de uso:
lista_de_numeros = [1, 2, 3, 4, 5]
resultado = extremos(lista_de_numeros)
print(resultado)  # Output: (1, 5)
```
**10-**
```
def primera_letra_mayuscula(tupla):
    return tuple(s.capitalize() for s in tupla)

# Ejemplo de uso:
mi_tupla = ("hola", "adios", "python")
resultado = primera_letra_mayuscula(mi_tupla)
print(resultado)  # Output: ('Hola', 'Adios', 'Python')
```

**Alumno**
Erubiel Cuevas Martinez
