# Escribir un programa para calcular las siguientes expresiones:
# a) 5√233
# b) |1 − 3𝑖|
# c) 𝑎𝑟𝑔(4 + 3𝑖)
# d) 𝑚𝑐𝑑(1260, 3846)

import numpy as np
import math as m

print('Resultado de la a:',pow(23**3,1/5))
print('Resultado de la b usando pow:',pow(1**2+(-3)**2,1/2))
print('Resultado de la b usando numpy:',np.sqrt(1**2 + (-3)**2))
print('Resultado de la b usando math:',m.sqrt(1**2 + (-3)**2))



