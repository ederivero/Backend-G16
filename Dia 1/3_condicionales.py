# if > si
edad = 30
nacionalidad = 'VENEZOLANO'

if edad > 18 and nacionalidad == 'PERUANO':
    print('Puedes votar')

# else > sino
else:
    print('Llamare a tus padres')


if edad > 18 or nacionalidad == 'PERUANO':
    print('Puedes votar')

# else > sino
else:
    print('Llamare a tus padres')


edad = 16
if edad > 18:
    print('Puedes votar')
# elif sino si
elif edad > 15:
    print('Ya te falta poco para votar')

else:
    print('Que haces aqui?')


# Segun el sexo y la estatura hacer lo siguiente
# si es Masculino
    # si mide mas de 1.50 entonces indicar que no hay prendas
    # si mide entre 1.30 y 1.49 indicar que si hay ropa
    # si mide menos de 1.30 indicar que no hay prendas
# si es Femenino
    # si mide mas de 1.40 indicar que no hay prendas
    # si mide entre 1.10 y 1.49 indicar que si hay
    # si mide menos de 1.10 indicar que no hay

sexo = 'Masculino'
estatura = 1.35
# output > SI HAY ROPA


sexo = 'Masculino'
estatura = 1.80
# output > NO HAY ROPA

sexo = 'Femenino'
estatura = 1.20
# output > SI HAY ROPA

sexo = 'Femenino'
estatura = 1.08
# output > NO HAY ROPA


if sexo == 'Masculino':
    if estatura > 1.30 and estatura < 1.49:
        print('Si hay Ropa')
    else:
        # si la persona mide mas de 1.5 o menos de 1.3
        print('No hay Ropa')
elif sexo == 'Femenino':
    # sexo = 'Femenino'
    if estatura > 1.10 and estatura < 1.40:
        print('Si hay ropa')
    else:
        print('No hay ropa')
        # o usamos el pass o colocamos la logica
        # pass > pasa (no hace nada pero nos permite dejar la condicional vacia)
        pass


# Operador TERNARIO
# condicion que sirve para ejecutarse en una sola linea y en base a la condicion RETORNARA un valor u otro

# Si el usuario es PERUANO pagara 5 soles si es EXTRANJERO pagara 8 soles
nacionalidad = 'ECUATORIANO'

if nacionalidad == 'PERUANO':
    print('pague 5 soles')
else:
    print('pague 8 soles')

#           RESULTADO SI ES VERDADERO   if  CONDICIONAL(ES)          else RESULTADO SI ES FALSE
resultado = 'pague 5 soles' if nacionalidad == 'PERUANO' else 'pague 8 soles'

print(resultado)
