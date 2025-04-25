# Ejercicio 16: Contador de Números Pares e Impares
# Crea un programa que cuente y muestre la cantidad de números pares e impares en
# una lista ingresada por el usuario.


# defino el contador
def contador_pares_impares():
    print("Contador de pares e impares!")

    try:  # voy a pedir una lista de números separados por espacios para luego convertirla a números enteros
        lista_numeros = input("Introduce una lista de números separados por espacio: ")
        lista_numeros = [int(x) for x in lista_numeros.split()]

        # inicializo variables para pares e impares a 0
        pares = 0
        impares = 0    

        # cuento los números pares e impares con un bucle for
        for num in lista_numeros:
            if num % 2 == 0:  # los números son pares si su resto al dividirlos entre 2 es 0
                pares += 1
            else:
                impares += 1

        # Muestro el resultado
        print(f"En la lista hay un total de {pares} números pares y un total de {impares} números impares.")

    except ValueError:
        print("Por favor, introduce números enteros válidos en la lista.")

# invoco la funcion
contador_pares_impares()