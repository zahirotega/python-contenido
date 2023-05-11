'''
Si no sabe cuántos argumentos de palabras clave se pasarán a su función, agregue dos asteriscos: ** 
antes del nombre del parámetro en la definición de la función.

De esta forma, la función recibirá un diccionario de argumentos y podrá acceder a los elementos en consecuencia:
'''

def funcion(**kid):
  print("su apellido es " + kid["apellido"])

funcion(nombre = "Tobias", apellido = "Jimenez")