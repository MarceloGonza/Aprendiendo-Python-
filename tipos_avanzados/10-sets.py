# set significa grupo o conjunto
# se remueven los duplicados en los sets

primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)

# primer.remove(1)
# primer.add(5)


# print(primer | segundo)  # une los sets


# & devuelve los elementos que esten dentro del primero y el segundo
# print(primer & segundo)


# mostramos solamente los datos de la izquierda y quitamos los de la derecha
# print(primer - segundo)


# con alt + 94 hacemos el simbolo"caret"(^)
# diferencia simetrica, devuelve los elementos que se encuentren en el primero
# y en el segundo, pero que no se encuentren entre si(elimina los duplicados)
# print(primer ^ segundo)


# no podemos acceder a los elementos en los sets, pero si podemos preguntar:
if 5 in segundo:
    print("Hola Mundo")
