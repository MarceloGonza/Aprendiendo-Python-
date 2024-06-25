usuarios = [
    ["Felipe", 4],
    ["Santiago", 1],
    ["Gullyngham", 5]
]


# nombres = []

# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)
# se le conoce como map
# nombres = [usuario[0] for usuario in usuarios]
# print(nombres)


# filtrar (filter)
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# # filtrar y transformar
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
# print(nombres)


# con metodo map

nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

# con metodo filter

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
