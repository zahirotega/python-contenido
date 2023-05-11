'''
También puede enviar argumentos con la sintaxis clave = valor.

De esta manera el orden de los argumentos no importa.
'''

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")