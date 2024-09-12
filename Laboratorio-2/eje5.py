# Escribe un programa que pida primero un número par y luego un número impar
# (positivos o negativos). En caso de que uno o los dos valores no sea correcto, se
# mostrará un único aviso.

n1 = int(input("Ingrese un numero par: "))
n2 = int(input("Ingrese un numero impar: "))

if n1%2 != 0:
	print(n1,": El numero no es un part")
elif n2%2 == 0:
	print(n2, ": El numero no es impart")
else:
	print(n1,": es par")
	print(n2,": es impart")
