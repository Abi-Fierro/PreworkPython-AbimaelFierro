# Ejercicio 5: Suma de Números Pares
# Escribe un programa que calcule la suma de todos los números pares del 1 al 100.

# hago una variable para la suma

sumar_pares = 0

# uso un bucle for para recorrer los numeros del 1 al 100 y que se sumen en el contador de la variable

for numero in range(1, 101): #segun la explicación que me da el visualstudio el "stop es ommited" por lo que tengo que poner 101 para que pare de contar en el 100
  if numero  % 2 == 0: # si el resto de un numero dividido entre 2 da 0 el número es par.
    sumar_pares += numero

# muestro el resultado

print(sumar_pares); # me da 2550 supongo que está bien




