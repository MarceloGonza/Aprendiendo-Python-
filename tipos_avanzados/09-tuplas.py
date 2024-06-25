# es lo mismo que una lista, solo que no puede modificarse
# si pueden crearse nuevas

numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)
menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros  # desempaquetar
print(primero, segundo, otros)
for n in numeros:  # iteracion
    print(n)

listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito Feliz"
print(listaNumeros)
