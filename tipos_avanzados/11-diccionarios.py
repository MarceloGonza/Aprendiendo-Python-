# son una conexion de datos que se encuentran agrupados por una llave y un valor
# a la izquierda va un string, luego cualquier cosa
# las llaves son los strings
punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])


punto["z"] = 45
# print(punto, punto["lala"]) # preguntamos si algo existe
if "lala" in punto:
    print("encontre lala", punto["lala"])

# para aceder a un valor del diccionario
print(punto.get("x"))
# podemos pasarle un valor por defecto si no existe
print(punto.get("lala", 97))
# eliminar
del (punto["y"])

print(punto)
punto["X"] = 25

# iterar los valores
# no es necesario esta sintaxis
# for valor in punto:
#     print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)


# ejemplo real
usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Marcelo"},
    {"id": 4, "nombre": "Gonzalez"},
]

for usuario in usuarios:
    print(usuario["nombre"])
