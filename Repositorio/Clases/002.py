class Animal:
  def __init__(self, nombre, edad, especie):
    self.especie = especie
    self.name = nombre
    self.age = edad

animal = Animal("John", 10, "Perro")

print(f"Hola, mi nombre es {animal.name} y tengo {animal.age} años de edad y soy un {animal.especie}")