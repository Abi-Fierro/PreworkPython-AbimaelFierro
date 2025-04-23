# Ejercicio 4: Contador de Vocales
# Crea un programa que cuente el número de vocales en una palabra ingresada por el
# usuario.

# solicito una palabra con un input
palabra = input("Ingresa una palabra :) ")

# defino las vocales
vocales = "aeiouAEIOU"

# defino el contador fuera del bucle
contador = 0

# hago un bucle for para recorrer la palabra que se ponga en el input y cuento las vocales que hay en la palabra
for letra in palabra:
    if letra in vocales:
        contador += 1

# muestro el resultado
print(f"La palabra '{palabra}' tiene {contador} vocal/es!")
