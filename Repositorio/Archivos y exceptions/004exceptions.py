'''
Puede definir tantos bloques de excepción como desee,
si desea ejecutar un bloque especial de código para un tipo especial de error:



try:
  print(x)
except:
  print("An exception occurred")
  
  '''
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

  
