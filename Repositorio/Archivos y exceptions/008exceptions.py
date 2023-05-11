#Index error
mi_lista = ["Python","C","C++","JavaScript"]
buscar_indice = -2 #probar con numeros negetivos
try:
  print(mi_lista[buscar_indice])
except IndexError:
  print("Lo siento, el indice esta fuera de rango")