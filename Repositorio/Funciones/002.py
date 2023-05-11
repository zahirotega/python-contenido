'''
La información se puede pasar a funciones como argumentos.

Los argumentos se especifican después del nombre de la función, entre paréntesis. 
Puede agregar tantos argumentos como desee, simplemente sepárelos con una coma.

El siguiente ejemplo tiene una función con un argumento (name). Cuando se llama a la función, 
pasamos un nombre, que se usa dentro de la función para imprimir el nombre completo:
'''
def funcion(name):
  print(" Mi nombre es " + name)

funcion("Emilio")
funcion("Tobias")
funcion("Luis")

print("Mi nombre es  Emilio")
print("Mi nombre es  Tobias")
print("Mi nombre es  Luis")