# Ejercicio 7: Calculadora Simple
# Crea un programa que realice operaciones aritméticas simples (suma, resta,
# multiplicación, división) según la elección del usuario.

#primero hay que definir la calculadora...
def calculadora(): 
    print("Calculadora Simple")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Elige una opción (1/2/3/4): ") #input para seleccionar una de las opciones de la calculadora.

    if opcion in ('1', '2', '3', '4'):
        try: #con el try me aseguro que el numero sea int para poder hacer los calculos básicos
            num1 = int(input("Introduce el primer número: "))
            num2 = int(input("Introduce el segundo número: "))
            if opcion == '1': #if para la primera opcion
                print(f"El total de la suma es: {num1 + num2}")
            elif opcion == '2': #uso elif para las demás opciones
                print(f"El total de la resta es: {num1 - num2}")
            elif opcion == '3':
                print(f"El total de la multiplicación es: {num1 * num2}")
            elif opcion == '4':
                    print(f"El total de la división es: {num1 / num2}")
        except ValueError: #la excepción del try por si no se ponen numeros enteros...
            print("Por favor, introduce valores numéricos enteros válidos.")
    else:
        print("Opción no válida.")

# ejecuto la calculadora
calculadora()