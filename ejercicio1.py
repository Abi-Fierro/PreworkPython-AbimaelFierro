# Ejercicio 1: Conversor de Temperatura
# Escribe un programa que convierta una temperatura de grados Celsius a grados
# Fahrenheit.

#    De ºC a ºF: se multiplica por 1.8 y se suma 32.
#     De ºF a ºC: se resta 32 y se divide entre 1.8.
#     De ºC a K: se suma 273.15.
#     De K a ºC: se resta 273.15.
#     De ºF a K: se suma 459.67 y se divide entre 1.8.
#     De K a ºF: se multiplica por 1.8 y se resta 459.67.


def c_to_f(temperatura):
  return temperatura * 1.8 + 32;

temperatura_c = 20
temperatura_f = c_to_f(temperatura_c)
print(f'{temperatura_c}º C son {temperatura_f} Fahrenheit');


temperatura_c = 50
temperatura_f = c_to_f(temperatura_c)
print(f'{temperatura_c}º C son {temperatura_f} Fahrenheit');
