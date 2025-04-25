# Ejercicio 14: Calculadora de Descuento
# Crea un programa que calcule el precio final de un artículo después de aplicar un
# descuento del 20%.


def calculadora_descuento():
    print("Calcula tu descuento del 20%! ")
    try: #aprovecho y ya que estamos, pediré las cosas por inputs en vez de definirlas manualmente...
        precio_original = float(input("Introduce el precio original del artículo: "))
        descuento = precio_original * 0.20  # calculamos el 20% de descuento
        precio_final = precio_original - descuento  # Restamos el 20%
        print(f"El precio final después del descuento es de {precio_final:.2f} euros.")
    except ValueError:
        print("Por favor, introduce un precio válido.")

# invoco la función
calculadora_descuento()
