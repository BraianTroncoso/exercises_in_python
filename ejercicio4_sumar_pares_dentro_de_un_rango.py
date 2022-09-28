# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro
# de un rango, por ejemplo:
#                   suma de números pares del 2 al 30
#                   suma = 240
sum = 0
for i in range(2,32):
    if i % 2 == 0:
        sum += i


print(sum)

