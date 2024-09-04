# Escribe un programa que genere un string compuesto por los primeros 3
# caracteres y los últimos 3 caracteres de un string introducido por el usuario.
# Sugerencia: utilizar la función len() en la obtención de los últimos 3 caracteres.
#  Ejemplo 1: 'aprendiendo'
# Resultado 1: 'aprndo'
#  Ejemplo 2: 'escribiendo código'
# Resultado 2: 'escigo'

texto = input("Ingrese string: ")
print(texto[0],texto[1],texto[2],texto[-3],texto[-2],texto[-1])
