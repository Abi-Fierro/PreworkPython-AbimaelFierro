# Ejercicio 18: Contador de Palabras
# Ejercicios Introducción a Python: Enunciados3
# Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.

#defino el contador

def contador_palabras():
  print("Contador de palabras!")

  try:

    frase = input("Introduce una frase para poder contar las palabras: ") # en el caso de strings, no hace falta definir el tipo de dato en el input
    palabras = frase.split() # separo la frase en palabras
    cantidad_palabras = len(palabras)

    print(f"La frase tiene {cantidad_palabras} palabras!")

  except ValueError:
    print("No se pudo leer bien la frase, introduzcala de nuevo")


#invoco la funcion
contador_palabras()
