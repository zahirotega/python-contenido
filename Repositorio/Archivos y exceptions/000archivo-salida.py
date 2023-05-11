#archivo-salida.py

#open le dice a tu computadora que produzca un nuevo archivo de texto llamado holamundo.txt
#El parámetro w indica que pretendemos escribir contenido en este nuevo archivo utilizando Python.
f = open ('holamundo.txt','w') 
f.write('adios mundo')
f.close()


'''
El código que es más cercano a los requerimientos de la máquina se denomina de bajo nivel, 
mientras que el código que es más cercano al lenguaje propio de los seres humanos es llamado de alto nivel.

método” significa fragmentos de código que realizan acciones

Puedes intentar imaginar esto utilizando algún referente del mundo real como, por ejemplo,
          dar órdenes a tu perro que ha sido educado previamente. 
Tu mascota (el objeto) entiende órdenes (i.e. tiene “métodos”) como “ladra”, “sentado”, “echado” y así.

'''