

# edad = 15
# if edad > 54:
#     print("Puede ver la pelicula con descuento")
# elif edad > 17:
#     print("Pu
# edes ver la pelicula")
# else:
#     print("No puedes entrar")
#     print("Ve a
# otro lado")

# print("Listo")


# El codigo siempre se debe realizarse de arriba hacia abajo, en este caso primero pusimos el if con edad de 54
# porque de no hcaerlo, el codigo no se ejecuta correctamente y si empezaramos al reves poniendo la edad menor,
# el codigo nunca entraria a
# la condicion de 55 años


# Solicitar la edad del usuario


edad = int(input("¿Cuál es tu edad? "))

# Solicitar la serie que está viendo el usuario
serie = input("¿Qué serie estás viendo? ")

# Verificar las condiciones y mostrar mensajes apropiados
if edad > 25 and serie == "The Big Bang Theory":
    print("Usted si sabe divertirse")
elif edad > 25:
    print("No alcanza wey")
elif serie == "The Big Bang Theory":
    print("Its so cloosee")
else:
    print("Usted me da asco")
