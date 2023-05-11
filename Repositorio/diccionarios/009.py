'''
El método update() actualizará el diccionario con los elementos del argumento dado.
El argumento debe ser un diccionario o un objeto iterable con pares clave:valor
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})