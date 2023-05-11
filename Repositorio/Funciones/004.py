'''
*args

Si no sabe cuántos argumentos se pasarán a su función, agregue un * antes del nombre del parámetro en 
la definición de la función.

De esta manera, la función recibirá una tupla de argumentos y podrá acceder a los elementos en consecuencia:
'''

def funcion(kids, kids1, kids2):
  for valor in kids:
    print("El niño mas chico es " + valor) 

funcion("Emili", "Tobias", "diego")
