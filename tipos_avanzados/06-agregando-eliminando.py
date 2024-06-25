mascotas = ["Gatito",
            "Catito",
            "Perrito",
            "Conejito",
            "Catito"
            ]

mascotas.insert(1, "Iguana")  # agrega el elemento en el indice indicado
mascotas.append("Avestruz")  # agrega al final


mascotas.remove("Catito")  # elimina solo el primero(si esta repetido)
mascotas.pop()  # elimina el ultimo elemento, al menosque le pasemos indice
del mascotas[0]  # elimina en donde le indiquemos
mascotas.clear()  # elimina toda la lista
print(mascotas)
