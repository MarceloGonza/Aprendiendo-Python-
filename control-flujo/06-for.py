# for:

# for numero in range(5):
#     print(numero, numero * 'hola mundo')

# for else:

buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no se encontro el numero buscado")
