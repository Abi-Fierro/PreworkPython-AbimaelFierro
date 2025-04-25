# Ejercicio 9: Conversor de Divisas
# Ejercicios Introducción a Python: Enunciados2Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
# 1 dólar es igual a 0.85 euros.


#defino el conversor
def conversor_divisas():
    print("Conversor de Dólares a Euros")
    try: #try except para asegurar los valores que llegan por el input
        dolares = float(input("Introduce la cantidad en dólares: "))
        tasa_conversion = 0.85 #variable de la tasa de conversión en este caso 0.85 segun el ejercicio
        euros = dolares * tasa_conversion
        print(f"{dolares:.2f} dólares son {euros:.2f} euros.")
    except ValueError:
        print("Por favor, introduce una cantidad válida.")

# invoco la función
conversor_divisas()
