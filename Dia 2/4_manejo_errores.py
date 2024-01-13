numero = 10
# try (intentalo)
# y si es que falla entonces capturo el error con una except (excepcion)
try:
    print(10/'eduardo')
# si ingresa a un Except ya no ingresara a los demas siempre se recomienda dejar el Except mas generico (Exception) al final para evitar ingresos innecesarios
except ZeroDivisionError:
    # si el error es de tipo de division entre 0 entonces ingresara aca
    print('No se puede dividir entre 0')

except Exception as error:
    # ver que es el causante del error
    print(error.args)
    # ver
    print(type(error))
    print('Operacion incorrecta')


print('otro codigo')

# Lambda Function / Funciones Anonimas
# esta funcion ademas no puede tener mas de una linea de codigo
# funcion no recibe ningun parametro y retorna el valor de 1
resultado =lambda valor1, valor2, valor3: valor1 + valor2 + valor3
print(resultado(10,20,30))

# Crear una funcion que reciba dos numeros y devuelva cual es el mayor, si el usuario ingresar un valor que no sea un numero entonces volver a pedirselo hasta que sea un numero
def numeroMayor(numero1, numero2):
    # forma 1
    if numero1 > numero2:
        return numero1
    else:
        return numero2

    # forma 2
    return numero1 if numero1 > numero2 else numero2

# pista: utilicen un while, un if y un try - except
while True:
    try:
        numero1 = int(input('Ingresa el primer numero:'))
        numero2 = int(input('Ingresa el segundo numero:'))
        # resultado = numeroMayor(numero1, numero2)
        resultado = lambda numero1, numero2: numero1 if numero1 > numero2 else numero2
        print('El numero mayor es {}'.format(resultado(numero1,numero2)))
        break
    except:
        print('Tienes que ingresar solo numeros')
