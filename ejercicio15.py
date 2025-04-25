# Ejercicio 15: Conversor de Tiempo
# Escribe un programa que convierta un número de minutos en horas y minutos. Por
# ejemplo, 145 minutos serían 2 horas y 25 minutos.

# defino el conversor

def conversor_horas():
  print("Conversor de minutos en horas!! (Y minutos :))")
  try: #try except para asegurar que el input es integer
    minutos = int(input("Introduce el número de minutos please "))
    #los calculos del programa
    horas = minutos // 60 # Divido los minutos que se introducen por 60 para determinar el número de horas
    mitnuso_restantes = minutos % 60 # Calculos los minutos que sobran de dividir los minutos entre 60

    #imprimo el resultado
    print(f"{minutos} minutos corresponde a {horas} horas y {mitnuso_restantes} minutos")
  except ValueError:
    print("Por favor introduce un precio válido.")


# invoco la función
conversor_horas()