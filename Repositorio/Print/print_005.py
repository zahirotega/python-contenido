
class Person:
    def __init__ (self, name):
        self.name = name
    def talk(self):
        print("Estoy imprimiendo una función")
            
john = Person("John Wick")
print(f'voy a imprimir el atributo nombre: {john.name}')
john.talk()