# Ejercicio 13: Verificación de Número Primo
# Escribe un programa que determine si un número ingresado por el usuario es primo
# o no.

# los numeros primos son numeros que solo pueden dividirse por 1 y por ellos mismos sin dejar residuo
# por lo visto si es menor que 2 nunca puede ser primo y un ejemplo de numero primo es el 7

#defino la calculadora
def es_numero_primo():
    print("Verificación de número primo")
    try: #try except parra asegurarr que el input me llega integer
        numero = int(input("Introduce un número para verificar si es primo: "))

        # Si el número es menor que 2, no puede ser primo
        if numero < 2:
            print(f"{numero} no es un número primo.")
            return
        
        # Por lo visto hay que verificar si el número es divisible por cualquier número entre 2 y la raíz cuadrada de numero
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                print(f"{numero} no es un número primo.")
                return
            
        print(f"{numero} es un número primo.")
    except ValueError:
        print("Por favor, introduce un número entero válido.")

# invoco la función
es_numero_primo()
