# Ejercicio 17: Conversor de Millas a Kilómetros
# Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
# que 1 milla equivale a 1.60934 kilómetros.

#defino la calculadora o conversor
def conversor_millas_km():
  print("Conversor de millas a kilómetros!")

  try:
    millas = float(input("Introduce el número de millas: "))
    # hago el calculo segun el enunciado
    kilometros = millas * 1.60934
    print(f"{millas} millas son {kilometros} kilometros.")
  except ValueError:
    print("Introduce un valor numérico válido de millas para poder calcular los km")

#invoco la funcion
conversor_millas_km()