# Escribe un programa que pida dos números enteros y que calcule su división,
# escribiendo si la división es exacta o no.


n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese primer numero: "))

divicion = n1/n2

resto =n1%n2

print("Numero 1: ", n1)
print("Numero 2: ", n2)
print("Divicion: ",divicion)

if resto == 0:
	print("La divicion exata")
else:
	print("La divicion no es exacta")



