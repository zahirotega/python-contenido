'''
Con la instrucción continuar podemos detener la iteración actual y continuar con la siguiente:

'''

i = 0
while i < 6:
  i += 1
  if i == 5:
    continue #Omite las sentnecias siguientes  y sigue con la sigiente iteración
  print(i)