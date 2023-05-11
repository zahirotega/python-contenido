'''
El bloque finalmente, 
si se especifica, se ejecutará independientemente de si el bloque de prueba genera un error o no.
'''
try:
  print("hola")
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")