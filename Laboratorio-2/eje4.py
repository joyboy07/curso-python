# Escribir el código en Python de la solución a la ecuación de segundo grado:
# ax2 + bx + c = 0. Revise el Pseudocódigo de la página 74 del pdf de la sesión de
# clase 04.

def ecuacion(a, b, c):
    if a == 0:
        if b != 0:
            x1 = -c / b
            print(f"x1 = {x1}")
        else:
            if c != 0:
                print('No solución!')
            else:
                print('Solución infinita')
    else:
        arg = b**2 - 4 * a * c
        if arg < 0:
            print('No solución real!')
        else:
            x1 = (-b + arg**(1/2)) / (2 * a)
            x2 = (-b - arg**(1/2)) / (2 * a)
            print(f"x1 = {x1}, x2 = {x2}")

print(ecuacion(1, -3, 2))
print(ecuacion(0, 2, -4))
print(ecuacion(0, 0, 5))
print(ecuacion(0, 0, 0))

