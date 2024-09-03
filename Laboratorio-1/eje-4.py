# Escribe un programa que pida el nombre de una persona y un número entero e
# imprima por pantalla en líneas distintas el nombre de la persona tantas veces
# como el número introducido.

nombre = input("Ingrese su nombre: ")
numeroEntero = int(input("Ingrese un numero entero: "))


for i in range(numeroEntero):
	print(nombre)


