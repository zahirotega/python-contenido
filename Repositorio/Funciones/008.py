'''
Puede enviar cualquier tipo de datos de argumento a una función (cadena, número, lista, diccionario, etc.),
y se tratará como el mismo tipo de datos dentro de la función.

P.ej. si envía una Lista como argumento, seguirá siendo una Lista cuando llegue a la función:
'''

def frutas(food):
  for x in food:
    print(f"Esta fruta es una {x}")

lista_frutas = ["manzana", "banana", "pera"]

frutas(lista_frutas)