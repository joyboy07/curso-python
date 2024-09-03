# Escribe un programa que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por
# pantalla la frase: Tu índice de masa corporal es <imc>; donde <imc> es el
# índice de masa corporal calculado redondeado con dos decimales.
# altura = 1.78
# peso = 77

peso = int(input('Ingrese su pedo en kg: '))

estatura = float(input('Ingrese estatura en metros: '))

imc = peso/estatura

print("Tu índice de masa corporal es: ", round(imc,2))


