# Escribe un programa que pida al usuario dos números enteros y muestre por
# pantalla la <a> entre <b> da un cociente <c> y un resto
# <r>; donde <a> y <b> son los números asignados por el usuario,
# y <c> y <r> son el cociente y el resto de la división entera, respectivamente.

a = int(input('Ingrese primer numero: '))

b = int(input('Ingrese segundo numero: '))

c = a/b

r = a%b

print("a: ", a)
print("b: ", b)
print("c: ", c)
print("r: ", r)

