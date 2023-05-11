# Modificar propiedades de objetos
class Carro: #Nuestra clase carro
  def __init__(self, color, numero_llantas):
    self.color = color
    self.llantas = numero_llantas

  def acelerar(self):
    print("El carro está acelerando")
    
  def frenar(self):
    print("El carro está frenando")
#Comienza bloque que se ejecutará
p1 = Carro("Rojo", 4)
print (p1.color)
p1.color = "Blanco" #Hacemos el cmabio aquí
print (p1.color)

del p1.color #(Elimina  atributo)
print (p1.color)