# Sea 𝑥 = (−1.24,0.24,−2.9,6.7,−0.56), ¿qué obtendremos al utilizar 𝑐𝑒𝑖𝑙(𝑥), 𝑓𝑖𝑥(𝑥),
# 𝑓𝑙𝑜𝑜𝑟(𝑥) 𝑦 𝑟𝑜𝑢𝑛𝑑(𝑥)? Escriba el programa.
import numpy as np

x = np.array([-1.24, 0.24, -2.9, 6.7, -0.56])

ceil_x = np.ceil(x)
fix_x = np.fix(x)
floor_x = np.floor(x)
round_x = np.round(x)

print("Resultado: ",ceil_x, fix_x, floor_x, round_x)







