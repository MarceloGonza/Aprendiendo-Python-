mensaje = "Bienvenidos a la calculadora"
mensaje1 = "Para salir escriba Salir"
mensaje2 = "Las operaciones que puede ingresar son suma, resta, multiplicacion y division"

print(mensaje)
print(mensaje1)
print(mensaje2)

n1 = input("Ingrese un numero: ")
op = input("ingrese una operacion: ")
n2 = input("Ingrese el regundo numero: ")

n1 = int(n1)
n2 = int(n2)

if op == "+":
    print("EL resultado es", n1 + n2)
elif op == "-":
    print("EL resultado es", n1 - n2)
elif op == "*":
    print("EL resultado es", n1 * n2)
elif op == "/":
    print("EL resultado es", n1 / n2)
else:
    print("Ingrese la oeracion correctamente")
