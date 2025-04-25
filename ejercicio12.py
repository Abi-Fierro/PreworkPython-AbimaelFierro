# Ejercicio 12: Calculadora de Área de un Rectángulo
# Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
# longitud y el ancho del rectángulo.

# la formula es:
# area = longitud x ancho

#defino la calculadora
def calculadora_area_rectangulo():
    print("Calculadora de área de un rectángulo")
    try: #try except para asegurar los inputs, en este caso los voy a poner floats.
        longitud = float(input("Introduce la longitud del rectángulo: "))
        ancho = float(input("Introduce el ancho del rectángulo: "))
        # Calcular el área según la fórmula
        area = longitud * ancho
        print(f"El área del rectángulo es: {area:.2f}.")
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")

# Llamada a la función
calculadora_area_rectangulo()
