# Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
# no. 
# segun internet se deben cumplir una de estas dos condicioneS
# el año es divisible por 4 pero no por 100
# el año es divisible por 400


#defino la funcion para verificar


def verificador_anyo_bisiesto(): #no se si la puede influir asi que mejor no lo pongo
  print("Verificador de años bisiestos")

  try:
      anyo = int(input("Introduce el año para calcular si es o no bisiesto "))

      # verifico con el calculo si es bisiesto o no

      if (anyo % 4 == 0 and anyo % 100 !=0) or (anyo % 400 == 0):
         print("El año SI es bisiesto!")
      else:
         print ("El año NO es bisiesto :(")
  
  except ValueError:
    print("Error de dato, introduce el año en números enteros en formato 'XXXX'")

#invoco la funcion
verificador_anyo_bisiesto()
