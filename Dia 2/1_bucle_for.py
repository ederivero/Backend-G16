alumnos = ['Angel', 'Bryan', 'Carlos', 'Hiroito', 'Claudia', 'Samael', 'Marco']


for alumno in alumnos:
    print(alumno)


# for se puede utilizar con string (textos)
frase = 'No hay mal que por bien no venga'

for letra in frase:
    # imprimir el texto pero sin espacios
    # Forma 1
    # pista: usar el if y el pass
    if letra == ' ':
        pass
    else:
        print(letra)

    # Forma 2
    # pista: usar el if sin el else
    if letra != ' ':
        print(letra)

    # Forma 3
    # continue > termina el ciclo actual (la iteracion en camino) y no permite hacer nada mas luego
    # del continue
    # continue solo se puede utilizar dentro de un loop (FOR, WHILE)
    if letra == ' ':
        continue
    print(letra)

    # Forma 4
    # operador ternario SOLO SE PUEDE colocar en sus resultados PALABRAS NO CLAVE
    # None > nada / nadie
    # Para definir una variable y esta no queremos colocarle un valor inicial podemos usar la palabra None
    # Si no queremos realizar nada en un operador ternario podemos colocarlo ahi
    None if letra == ' ' else print(letra)


# la variable edad tiene un contenido vacio , esto en Javascript seria como undefined
edad = None

print('--------------------------------')
# range > si quiero realiza un for manual sin uso de listas, tuplas, set o textos
# range(limite) > el for se ejecutara hasta que el valor sea menor que el tope (limite)
for numero in range(4):
    print(numero)

print('----')
# range(inicio, limite)
for numero in range(1, 4):
    print(numero)

print('------')
# range(inicio, limite, incrementa / decrementa)
for numero in range(1, 10, 2):
    print(numero)


texto = 'Hola me llamo eduardo'
vocales = ['a', 'e', 'i', 'o', 'u']

print('j' in vocales)
print('e' in vocales)

# Iterar la variable texto y ver cuantas vocales hay
# Respuesta: Hay 9 vocales

# incrementador
contador = 0

for letra in texto:
    if letra in vocales:
        # al valor anterior del contador le sumamos 1
        contador = contador + 1

# Estas son las formas de imprimir un texto combinado con variables

print('Hay', contador, 'vocales')

# {} > que donde tengamos {} ahi colocaremos una variable que puede ser numero, texto ,bool, etc
print('Hay {} vocales'.format(contador))

# al colocar la f antes de las comillas estaremos indicando que lo que vaya dentro de las llaves sera codigo python dentro de ellas podemos utilizar variables y operaciones
print(f'Hay {contador} vocales')

# %s que convierta el valor que le vamos a pasar a un formato texto
print('Hay %s vocales' % (contador))


# %
print(99/5)  # cociciente
print(99 % 5)  # residuo entero
print(99 // 5)  # cociente entero sin el uso de decimales

# Utilizando range realice
range(1, 56)
# quiero saber cuantos numeros pares tengo
# Resultado: Hay 27 numeros pares
numero % 2 == 0  # es un numero par

contador = 0
for numero in range(1, 56):
    if numero % 2 == 0:
        # contador = contador + 1
        contador += 1


print('Hay', contador, 'numeros pares')
