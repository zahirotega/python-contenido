'''
Métodos tuplas

'''
#El método count() cuenta el número de veces que el objeto pasado como parámetro se ha encontrado en la lista.
l = [1, 1, 1, 3, 5]
print(l.count(1)) #3
#Ejemplo de count con texto
nombre="maria"
print(nombre.count("a"))

#El método index() busca el objeto que se le pasa como parámetro y devuelve el índice en el que se ha encontrado.
l = [7, 7, 7, 3, 5]
print(l.index(5)) #4