import math

print(round(1.3))  # devuelve el numero que se encuentre mas cerca del que le pasemos
print(round(1.7))
print(abs(-55))
# print entrega el valor absoluto del numero que le pasemos a la funcion(siempre devuelve positivo)

# modulo nativo de python para trabajar con numeros: MATH

# toma el numero y lo lleva al numero superior entero mas cercano
print(math.ceil(1.2))
print(math.floor(1.9999))  # lo lleva al entewro inferior mas cercano

# isnan nos devuelve si es que el valor que le estamos pasando corresponde a que NO es un numero
print(math.isnan(23))
print(math.pow(10, 3))  # pow nos permite elevar un numero a la potencia de algo

print(math.sqrt(9))  # sqrt saca  la raiz cuadrada del numero que le pasemos
