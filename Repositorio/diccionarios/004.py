'''
             Colecciones de Python (matrices)

Hay cuatro tipos de datos de recopilación en el lenguaje de programación Python:

-La lista es una colección ordenada y modificable. Permite miembros duplicados.
-Tuple es una colección ordenada e inmutable. Permite miembros duplicados.
-Conjunto es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
-El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.

'''

'''
                   Acceso a objetos del diccionario


'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#x = thisdict["model"]


#Otra manera de hacerlo
#x = thisdict.get("model")
#print(x)

#Keys() metodo retorna un alista  de los valores claves en el diccionario
y = thisdict.keys()
print(y)