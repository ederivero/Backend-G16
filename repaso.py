def sumar(num1, num2):
    return num1 + num2


resultado = sumar(num1=10, num2=20)
print(resultado)

data = {
    'num1': 10,
    'num2': 20
}

resultado = sumar(num1=data.get('num1'), num2=data.get('num2'))

print(resultado)

# cuando el nombre de la llave del diccionario es el mismo que el nombre del parametro de la funcion
# al utilizar el ** este agarrara el diccionario y sacara las llaves y las convertira a parametros y sus valores a los valores de esos parametros
# **data => num1=10, num2=20
resultado == sumar(**data)
print(resultado)


data = {
    'numero1': 10,
    'numero2': 20,
}
resultado == sumar(**data)
print(resultado)
