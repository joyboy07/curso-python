# Sea 𝑥 = (1, 4, 6, 5, 8, 9, 10, 2, 5, 6, 8), escribir un programa para calcular:
#  El logaritmo neperiano de cada elemento de x.
#  El logaritmo decimal de cada elemento de x.
#  El logaritmo en base 2 de cada elemento de x.
#  La raíz cuadrada de cada elemento de x.
#  La potencia de base 10 de cada elemento de x.
#  La potencia de base e de cada elemento de x.
#  La potencia de base 2 de cada elemento de x.

import numpy as np

x =(1, 4, 6, 5, 8, 9, 10, 2, 5, 6, 8)

# El logaritmo neperiano de cada elemento de x.
rest1 = np.log(x)
print('El logarimo nepereano es numpy: ', list(rest1))

# El logaritmo decimal de cada elemento de x.

rest2 = np.log10(x)
print('El logaritmo decimal es: ', list(rest2))

# El logaritmo en base 2 de cada elemento de x.

rest3 = np.log2(x)
print('El logaritmo en base 2 es: ', list(rest3))

# La raíz cuadrada de cada elemento de x.

rest4 = np.sqrt(x)
print('La raiz cuadrada es: ', list(rest4))

# La potencia de base 10 de cada elemento de x.
rest5 = np.power(10,x)
print('La potencia de base 10 es: ', list(rest5))

# La potencia de base e de cada elemento de x.

rest6 = np.exp(x)
print('La potencia de base e es: ', list(rest6))
# La potencia de base 2 de cada elemento de x.

rest7 = np.power(2,x)
print('La potencia de base 2 es: ', list(rest7))

