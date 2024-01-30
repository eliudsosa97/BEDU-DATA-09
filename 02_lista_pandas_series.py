import pandas as pd

lista_numeros = [1, 2, 3, 4, 5]
print(type(lista_numeros))
serie_numeros = pd.Series(lista_numeros)
print(type(serie_numeros))
print(serie_numeros)