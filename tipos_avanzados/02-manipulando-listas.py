mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0])
mascotas[0] = "Bicho"  # cambia el primer elemento
print(mascotas[2:])  # desde dond arranca el array

# [-1] como no hay nada a la izquierda, va al final del array (copito)
print(mascotas[-1])


# toma el primero, saltea el segundo, toma el siguiente, el proximo lo saltea(1 en 1)
print(mascotas[::2])

print(mascotas[1::2])  # saltea el primero, toma el siguiente, etc

# si tuviera mas elementos le indicamos hasta donde queremos llegar
print(mascotas[1:2:2])


# numeros = list(range(1,21)) # le indicamos que empieze de 1
numeros = list(range(21))
print(numeros[::2])  # me devuelve los pares


# devuelve los impares porque le indicamos de donde empieza a imprimir
print(numeros[1::2])
