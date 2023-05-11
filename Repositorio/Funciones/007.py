'''
Valor de parámetro predeterminado
El siguiente ejemplo muestra cómo utilizar un valor de parámetro predeterminado.

Si llamamos a la función sin argumento, usa el valor predeterminado:
'''
def my_function(country = "México"):
  print("Yo soy de  " + country)

my_function("Ecuador")
my_function("Francia")
my_function()
my_function("Brasil")