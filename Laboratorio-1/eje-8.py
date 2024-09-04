# Escribe un programa que cree un diccionario vacío y lo vaya llenado con
# información sobre una persona (por ejemplo, nombre, edad, sexo, teléfono,
# correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un
# nuevo dato debe imprimirse el contenido del diccionario.

persona = {}

nombre = input("Ingrese nombre: ")
edad = input("Ingrese edad: ")
sexo = input("Ingrese sexo: ")
telefono = input("Ingrese telefono: ")
correo = input("Ingrese correo electronico: ")

persona["nombre"] = nombre
persona["edad"] = edad
persona["sexo"] = sexo
persona["telefono"] = telefono
persona["correo"] = correo

print(persona)

