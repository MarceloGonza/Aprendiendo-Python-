def hola(nombre, apellido="Insano"):
    print("Hola mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola("Marcelo", "Gonzalez")
hola("Choclo")


# tambien podemos indicarle a la funcion que argumentoes, en caso que el orden no este dado o tengamos
# que realizarlo asi previamente

hola(apellido="Gonzalez", nombre="Marcelo")
