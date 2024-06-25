numeros = [1, 67, 14, 23, 56, 95, 11]

# numeros.sort()  # ordena de menor a mayor
# numeros.sort(reverse=True)  # de mayor a menor
# sorted(numeros)  # devuelve una nueva lista(no afecta el listado anterior)

numeros2 = sorted(numeros)  # tambein se puede utilizar el reverse
print(numeros)
print(numeros2)

usuario = [[4, "Felipe"],
           [1, "Santiago"],
           [5, "Gullyngham"]
           ]

usuario.sort()
print(usuario)

# si el numero esta al final, tenemos que indicarle a sort
usuario = [
    ["Felipe", 4],
    ["Santiago", 1],
    ["Gullyngham", 5]
]


# puede usarse el reverse tambien
usuario.sort(key=lambda el: el[1])
print(usuario)
