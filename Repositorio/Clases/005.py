class Carro:
  def __init__(self, color, numero_llantas):
    self.color = color
    self.llantas = numero_llantas

  def acelerar(self):
    print("El carro está acelerando")
    
  def frenar(self):
    print("El carro está frenando")

carro = Carro("Rojo", 4)
carro.frenar()