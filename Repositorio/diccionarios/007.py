'''
Realice un cambio en el diccionario original y vea que la lista de elementos también se actualice:
'''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
print(car)