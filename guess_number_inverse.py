import random

number = random.randrange(1,50)

guess = int(input('Ingresa un numero para que adivine la maquina (debe de ser entre 1 - 50)'))
count = 0

while guess != number:
    if guess<1 or guess>50:
        guess = int(input('Ingresa un numero para que adivine la maquina (debe de ser entre 1 - 50)'))
    else:
        count+= 1
        number = random.randrange(1,50)


String =  'La maquina tardo {} intentos en adivinar tu numero'.format(count)
print(String)