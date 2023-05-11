'''
Por defecto, una función debe llamarse con el número correcto de argumentos. 
Lo que significa que si su función espera 2 argumentos, debe llamar a la función con 2 argumentos, ni más ni menos.

Esta función espera 2 argumentos y obtiene 2 argumentos:
'''

def funcion(apellido, nombre):
  print(nombre + " " + apellido)

funcion(nombre ="Emilia", apellido ="Gutierrez")