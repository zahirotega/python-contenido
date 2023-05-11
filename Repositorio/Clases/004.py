# Con __str__

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    saludo =  f"Me llamo {self.name} y mi edad es {self.age}"
    return saludo
  
  

p1 = "0x0000020B8C7F7D60"

print(p1)