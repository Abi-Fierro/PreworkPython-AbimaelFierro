# Ejercicio 11: Calculadora de Edad
# Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
# actual.


#defino la calculadora
def calculadora_edad():
    print("Calculadora de edad")
    try: #try y except para asegurar el input para obtener el año de nacimiento y el actual
        nacimiento = int(input("Introduce tu año de nacimiento: "))
        año_actual = int(input("Introduce el año actual: "))
        # Calcular la edad
        edad = año_actual - nacimiento
        print(f"Tu edad es: {edad} años.")
    except ValueError:
        print("Por favor, introduce un año válido.")

# invoco la función
calculadora_edad()
