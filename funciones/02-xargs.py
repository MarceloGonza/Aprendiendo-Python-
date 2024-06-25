# el* significa que algo es iterable(se le puede aplicar el for para recorrerlos)
# siempre tener en cuenta la identacion
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)
