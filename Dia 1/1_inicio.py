nombre = 'Eduardo'
nombre = 12
nombre = False
nombre = '2023-12-12'

# Creo la variable para indicar el estado civil de la persona
soltero = False

# El comentario es muy importante para mantener nuestro codigo documentado
print(nombre)

numero1 = 10

numero2 = 40

print(type(numero1))
# Si queremos realizar una sumatoria entre un texto y un numero no es posible
# Si la sumatoria se realiza entre dos string (texto) esta sera una concatenacion
resultado = numero1 + numero2

print(resultado)

numero1 = '80'
numero2 = "40"

resultado = numero1 + numero2

print(resultado)


# Para convertir de un tipo de dato a otro utilizo el tipo de dato que quiero convertir
# tengo que estar seguro que el valor fuente pueda ser convertido
convertir_entero = int(numero1)

print(type(convertir_entero))


# TIPOS DE VARIABLES EN PYTHON

# INT (enteros)
numero = 10

# FLOAT (flotantes)
# Si ponemos coma esto se puede confundir con un tipo de dato especial (ARREGLO, TUPLA, DICCIONARIO, SET)
calificacion = 10.4

# BOOLEAN (Boolean)
vacunado = False

# STRING (text)
nombre = 'eduardo"carnicero"'
nombre = "eduard'o"
texto = '''
Era una mañana de enero.
Los pajaros cantaban ...
'''
texto2 = """
Y en eso, una señora
Muy amablemente me sonrio y me dijo ¨....¨
"""
# si queremos que el texto contenga saltos de linea usamos la triple comilla o triple doble comilla

curso, grupo, mes, dia, hora, minutos = 'Backend', 'G16', 'Enero', 11, 20, 45

# FORMA DE DECLARAR VARIABLES, FUNCIONES, CLASES, METODOS
snake_case = 'snake_case'
nombre_completo = 'Eduardo de Rivero Manrique'

camelCase = 'camelCase'

PascalCase = 'PascalCase'
