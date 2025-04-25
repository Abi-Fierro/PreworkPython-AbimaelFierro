# Ejercicio 20: Suma de Números en una Lista
# Crea un programa que sume todos los números en una lista ingresada por el
# usuario.

# defino la calculadora para sumar

def sumador_lista():
  print("Te cojo una lista y te la sumo!!")

  try:
      lista = input("Introduce numeros enteros separados por espacios para poder sumarlos ")

      #convierto la lista de valores en una lista de numeros enteros
      lista_numeros = [int(x) for x in lista.split()]
      #sumo los numeros de la lista de numeros
      suma = sum(lista_numeros)
      #muestro el resultado
      print(f"La suma de los números que introdujiste es {suma}")
  except ValueError:
    print("Introduce números enteros en una lista y separalos por espacios para poder sumarlos")

#invoco la funcion
sumador_lista()