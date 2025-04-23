# Ejercicio 6: Verificación de Palíndromo
# Crea un programa que verifique si una palabra ingresada por el usuario es un
# palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

# input para ingresar una palabra.
palabra = input("Ingresa una palabra: ")

# comparo la palabra con un if, else usando slicing para comparar la misma palabra pero empezando desde el final usando slicing ::-1
if palabra == palabra[::-1]: # 
    print("La palabra sí es un palíndromo! :(")
else:
    print("La palabra no es un palíndromo! :(")
