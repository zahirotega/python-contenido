
#Input con conversión a enteros(input por default es texto)
#función para redondear y operación 
cantidad = int(input("Dígame una cantidad en pesos mexicanos: "))

print(f"{cantidad} pesos son {round(cantidad / 19.95656, 2)} dolares")