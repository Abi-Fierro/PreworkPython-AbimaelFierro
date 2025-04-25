# Ejercicio 10: Determinar el Día de la Semana
# Escribe un programa que determine el día de la semana correspondiente a un
# número ingresado por el usuario (1 para lunes, 2 para martes, etc.).


#defino la calculadora
def calcular_dia():
    print("Determina el Día de la Semana")
    try: #try y except para asegurar el input entero del 1 al 7
        numero = int(input("Introduce un número del 1 al 7: "))
        dias = {
            1: "Lunes",
            2: "Martes",
            3: "Miércoles",
            4: "Jueves",
            5: "Viernes",
            6: "Sábado",
            7: "Domingo"
        }
        if numero in dias:
            print(f"El día correspondiente es: {dias[numero]}")
        else:
            print("El número está fuera del rango. Debe ser del 1 al 7.")
    except ValueError:
        print("Por favor, introduce un número entero válido.")

# invoco la función
calcular_dia()
