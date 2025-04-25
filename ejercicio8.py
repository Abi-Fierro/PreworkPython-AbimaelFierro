# Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
# Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.

# La formula es:
# IMC = peso (kg)​ / altura (m)2


#defino la calculadora
def calculadora_imc():
    print("Cálculo del Índice de Masa Corporal (IMC)")

    try: #pongo un try de nuevo para asegurar que los valores que pido con el input sean float en este caso (para poder poner centimetros y gramos tambien)
        peso = float(input("Introduce tu peso en kilogramos: "))
        altura = float(input("Introduce tu altura en metros: "))
        if altura <= 0:
            print("La altura debe ser mayor que cero.")
        else:
            imc = peso / (altura ** 2)
            print(f"Tu IMC es: {imc:.2f}")
    except ValueError: #la excepción para el try
        print("Por favor, introduce valores numéricos válidos.")

# invocolamada la función
calculadora_imc()

