# while puede convertirse en un bucle infinito

numero = 10
# while se ejecutara hasta que la condicion sea verdadera
# while primero valida la condicion y luego ejecuta el codigo
while numero < 20:
    print('hola')
    print(numero)
    numero += 1

# en python no existe el do-while

# valor = input('Por favor ingresa un numero:')
# print(valor)

# Adivina el numero
numero = 225
numero_adivinado = 0
while numero_adivinado != numero:
    # todos los valores que le pasemos al input se capturaran como string
    numero_adivinado = int(input('Por favor ingresa un numero:'))
    # si me ingresa 20 entonces decirle que el numero es mayor
    # si me ingresa 250 entonces decirle que el numero es menor
    if numero_adivinado < numero:
        print('El numero es Mayor!')
    elif numero_adivinado == numero:
        print('Felicidades Acertaste!')
    else:
        print('El numero es Menor!')


while True:
    print('hola soy infinito')
    # para salir de un bucle ya sea for o while
    break
