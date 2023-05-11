def mas_10(num):
  return num + 10


try:
    mi_numero = int(input("Ingrese un numero: "))
except ValueError:
    try:
        resultado = mas_10(mi_numero)
    except NameError:
        print("El argumento `mi_numero` deberia ser un número")
