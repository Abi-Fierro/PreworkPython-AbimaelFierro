# Ejercicio 2: Calculadora de Propina
# Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
# una propina del 15% sobre el total de la cuenta.


def calcular_total_con_propina(cuenta):
    propina = cuenta * 0.15
    total = cuenta + propina
    return total

cuenta = 133  
total_a_pagar = calcular_total_con_propina(cuenta)

print(f'La cuenta es de {cuenta}€ y con la propina del 15% saldría {total_a_pagar}€')
