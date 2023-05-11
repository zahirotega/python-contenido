def main():
  numero = int(input("Dígame cuántas palabras tiene la lista: "))

  if numero < 1:
      print("¡Imposible!")
  else:
      lista = []
      for i in range(numero):
          palabra = input(f"Dígame la palabra {i + 1}: ")
          lista += [palabra]
      print(f"La lista creada es: {lista}")


if __name__ == "__main__":
  main()
  
  #Los archivos de Python se llaman módulos y se identifican mediante la extensión de archivo .py
  #cuando el intérprete ejecuta un módulo, el variable __name__ se establecerá como __main__