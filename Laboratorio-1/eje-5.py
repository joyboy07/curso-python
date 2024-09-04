# Una panadería vende barras de pan a S/. 3.49 cada una. El pan que no es el día
# tiene un descuento del 60%. Escribir un programa que comience leyendo el
# número de barras vendidas que no son del día. Después el programa debe
# mostrar el precio habitual de una barra de pan, el descuento que se le hace por
# no ser fresca y el coste final total.

precio = 3.49
descuento = 0.60
barrasVendidas = int(input("Imgrese Cantidad de barra vendidas que no son del dia: "))
print("Precio habitual: ",precio)
print("Descuento por no ser fresca: ",round((precio -( precio* descuento)),2))
print("Barra vendidas: ", barrasVendidas)
print("Coste final total: ", round (barrasVendidas *(precio* descuento),2))



