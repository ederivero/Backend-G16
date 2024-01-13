# Puedo agrupar varios valores en una variable

# Listas
# Que se puede modificar, es ordenada (maneja indices)
alumnos = ['Victor', 'Hiroito', 'Marco', 'Angel', 'Bryan', 'Samael', 'Claudia']

# Las listas empiezan con la posicion 0
print(alumnos[0])
print(alumnos[4])

# Para saber el contenido (longitud) de datos
# cuenta y no utiliza las posiciones
print(len(alumnos))

# Si queremos recorrer la lista de derecha a izq utilizaremos numeros negativos
print(alumnos[-1])

print(alumnos[len(alumnos)-1])

# agregar elementos a una lista ya creada
alumnos.append('Franklin')

print(alumnos)

# remover un elemento de la lista lo podemos guardar en una variable
alumno_eliminado = alumnos.pop(3)
print(alumnos)
print(alumno_eliminado)

# del > podemos eliminar variables, eliminar posiciones de la lista y otras cosas
del alumnos[0]
print(alumnos)
# cada vez que se elimina una posicion de la lista, todas las demas posiciones ocupan ese lugar disponible

# modificar el valor de una posicion de una lista
alumnos[0] = 'Eduardo'

# limpiamos toda la lista y la dejamos vacia
alumnos.clear()
print(alumnos)

# Las Listas pueden contener varios tipos de datos
mixto = ['Lunes', 10, False, 80.5, [1, 2, 3]]


ejercicio = [1, 2, 3, [4, 5, 6]]


# Devolver el valor de 3
print(ejercicio[2])
# Como puedo devolver el valor de 5
print(ejercicio[3][1])


# Tuplas
# No se puede modificar y es ordenada (indices)
# Se usa para guardar valores que jamas van a poder cambiar
meses = ('Enero', 'Febrero', 'Marzo', 'Abril')

print(meses[0])


data = ('Juan', 'Roberto', [1, 2, 3, ['Eduardo', 'Frank']])
# Obtener Eduardo
print(data[2][3][0])


# Set (Conjuntos)
# Desodernada y modificable
colores = {'Negro', 'Blanco', 'Guinda', 'Violeta'}

print(colores)
colores.add('Azul')
print(colores)

print('Verde' in colores)  # False > no esta contenido

colores.remove('Blanco')


# Diccionarios
# Ordenados PERO por llaves y modificables
persona = {
    'nombre': 'Eduardo',
    'edad': 31,
    'nacionalidad': 'PERUANO',
    'apellido': 'De Rivero',
}
print(persona.keys())  # LLAVES
print(persona.values())  # VALORES
print(persona['edad'])
# print(persona['edades']) # JAVASCRIPT si no existe me retorna undefined , aca lanza error

persona['nombre'] = 'Juancito'
persona['calzado'] = 'Zapatos'  # si la llave no existe, entonces la creara
print(persona)


persona = {
    'nombre': "Roberto",
    'edad': 40,
    'hobbies': ['Nada', 'Pescar', 'Jugar videojuegos'],
    'idiomas': [
        {
            'nombre': 'Ingles',
            'nivel': 'Intermedio'
        },
        {
            'nombre': 'Frances',
            'nivel': 'Basico'
        }
    ],
    'habilidades': {'Puntual', 'Economico', 'Proactivo'},
    'debilidades': ('Mentiroso', 'Resentido', 'Comelon')
}


# 1. Darme la Edad
print(persona['edad'])

# 2. Mostrar los hobbies
print(persona['hobbies'])

# 3. Mostrar el ultimo hobbie ingresado
print(persona['hobbies'][-1])

# 4. Mostrar los idiomas SOLO SUS NOMBRE
print(persona['idiomas'][0]['nombre'])
print(persona['idiomas'][1]['nombre'])

# 5. Ver si es Proactivo > True o False
print('Proactivo' in persona['habilidades'])

# 6. Ver cuantas debilidades tiene (cantidad)
print(len(persona['debilidades']))
