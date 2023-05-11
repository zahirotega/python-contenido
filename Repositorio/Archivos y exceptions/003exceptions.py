while True:
    #Primero, se ejecuta la cláusula try (la(s) linea(s) entre las palabras reservadas try y la except)
    try:
        try:
            x = int(input("Please enter a number: "))
            break #detiene los procesos (while y try)
        #Si no ocurre ninguna excepción, la cláusula except se omite y la ejecución de la cláusula try finaliza
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    except:
        print("")
    '''
    Si ocurre una excepción durante la ejecución de la cláusula try, se omite el resto de la cláusula. 
    Luego, si su tipo coincide con la excepción nombrada después de la palabra clave except, 
    se ejecuta la cláusula except, y luego la ejecución continúa después del bloque try/except.
    
    
    Si ocurre una excepción que no coincide con la indicada en la cláusula except se pasa a los try más externos;
    si no se encuentra un gestor, se genera una unhandled exception (excepción no gestionada) 
    y la ejecución se interrumpe con un mensaje como el que se muestra arriba.
    '''