


import pyreadstat

# Especifica la codificación que podría funcionar, como "ISO-8859-1" o "latin1"
df, meta = pyreadstat.read_sav('C:/Users/jporlles/Desktop/comercio_exterior/X_2024_II.sav', encoding='latin1')

# Imprime las primeras filas del dataframe
print(len(df.columns.tolist()))





