#En este ejemplo, el bloque try no genera ningún error:
try:
  print(x)
except:
  print("Something went wrong")
else: #Sejecuta si todo se cumple bien
  print("Nothing went wrong")