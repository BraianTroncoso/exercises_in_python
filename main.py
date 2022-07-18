# CLASE 1

# miVaraiable = 3
# print(miVaraiable)
# miVaraiable = 'Hola a todos los estudiantes'
# print(miVaraiable)
# miVaraiable = 3.5
# print(miVaraiable)
# x = 10
# y = 2
# z = x + y
# print(id(x))
#
# #ID
#
# print(id(y))
# print(id(z))
# ----------------------------------------------
# print('Hola mundo')
# ----------------------------------------------

# CLASE 2

# Dirección de memoria y variables

# miVariable = 3
# print(miVariable)
# miVariable = 'Hola a todos los estudiantes de la tecnicuatura'
# print(miVariable)
# miVariable = 3.5
# print(miVariable)
# x = 10
# y = 2
# z = x + y
# print(id(x))
# print(id(y))
# print(id(z))
# # Si redefino la direccion cambia
# x = 89
# print(id(x))

# CLASE 3

# rta = input('¿Cómo estuvo tu día?: ')

# print(f'Mi día estuvo de: {rta}')

# titulo = input('Proporciona el título: ')
# autor = input('Proporciona el autor: ')
# print(f'{titulo} fue escrito por {autor}')

# CLASE 4

#SUMA
# operandoA = 8
# operandoB = 5
# suma = operandoA + operandoB
# print(f'El resultado de la suma es {suma}')

# RESTA
# operandoA = 8
# operandoB = 5
# resta = operandoA - operandoB
# print(f'El resultado de la resta es {resta}')

# MULTIPLICACION
# operandoA = 2
# operandoB = 3
# multiplicacion = operandoA * operandoB
# print(f'El resultado de la multiplicacion es {multiplicacion}')

# DIVISION
# operandoA = 123
# operandoB = 12

# division = operandoA / operandoB
# print(f'El resultado de la division es {division}')
# divisionEntera = operandoA // operandoB
# print(f'El resultado de la division entera es {divisionEntera}')
# modulo = operandoA % operandoB
# print(f'El resultado del modulo es {modulo}')
# exponente = operandoA ** operandoB
# print(f'El resultado del exponente es {exponente}')

# PARIDAD
# a = int(input('Ingrese un numero: '))
# pariadad = a % 2 == 0
# if pariadad:
#     print(f'{a} es par')
# else:
#     print(f'{a} es impar')

# OPERADORES
# miVar *= 7
# miVar /= 3.4
# print(miVar)
#
# # Operadores COMPARACION
# # <=, >= , <, > ,== , !=
#
# miVar = 6 <= 3
# print('MENOR O IGUAL', miVar)
# miVar = 6 >= 4
# print('MAYOR O IGUAL', miVar)
# miVar = 6 < 5
# print('MENOR', miVar)
# miVar =  66 > 41
# print('MAYOR', miVar)
# miVar = 63 == 5
# print('IGUALDAD', miVar)
# miVar = 34 != 34
# print('DISTINTO', miVar)

# alto = int(input('Ingrese alto rectangulo: '))
# ancho = int(input('Ingrese ancho rectangulo: '))
#
# area = alto * ancho
# perimetro = 2*alto + 2*ancho
#
# print(f'El rectangulo con {alto} de alto y {ancho} de alto tiene un perimetro de {perimetro} y un area de {area}')

# ---------------------------------------------------------------------

# edadAdulto = 18
#
# edadPersona = int(input('Digite su edad: '))
# if edadPersona >= edadAdulto:
#     print(f'Su edad es : {edadPersona} años, usted es mayor de edad.')
# else:
#     print(f'Su edad es : {edadPersona} años, usted es menor de edad.')


#       CLASE 5

# RANGO EDAD
# edad = int(input('Ingrese su edad: '))
#
# en_20 = 20 <= edad < 30
# en_30 = 30 <= edad < 40
#
#
# if en_20 or en_30:
#     print("Esta en el rango")
# else:
#     print(f'No esta en el rango')
#-----------------------------------------------------------------
# num1 = int(input('Ingrese primer numero: '))
# num2 = int(input('Ingrese segundo numero: '))
#
# mayor = num1 if num1 > num2 else num2
#
# print(f'El mayor es {mayor}')

#-----------------------------------------------------------------
# vacaciones = True
# diaDescanso = True
#
# if not (vacaciones or diaDescanso):
#     print('Puede asistir al juego')
# else:
#     print('Tiene trabajo que hacer')
#
# # -----------------------------------------------------------------
# # Operadores LOGICOS
# # and, or , not
#
# miVar = 6 <= 3 and 5.4 == 5
# print('6 <= 3 and 5.4 == 5', miVar)
# miVar = 54 == 2 or 3.2 < 3.222
# print('54 == 2 or 3.2 < 3.222', miVar)
# miVar = not 4 <= 12
# print('not 4 <= 12 ', miVar)

#-----------------------------------------------------------------
# edad = 25
#
# if (20 <= edad < 30) or (30 <= edad <40):
#     print('Estas dentro del rango de los (20) a (30) años')
# else:
#     print('No estas dentro del rango de los (20) a (30) años')
#
# -------------------------------------------------------
# print('Ingrese los siguientes datos del libro')
# nombre = input('Ingrese nombre del libro: ')
# id = input('Ingrese ID del libro: ')
# precio = float(input('Ingrese precio del libro: '))
# envioGratuito = input('Indicar si el envio es gratuito (True/False)')
#
# if envioGratuito == 'True' or envioGratuito == 'T':
#     envioGratuito = True
# elif envioGratuito == 'False' or envioGratuito == 'F':
#     envioGratuito = False
# else:
#     envioGratuito = 'El valor ingresado es incorrecto'
#
# print(f'''
# Nombre : {nombre}
# Id : {id}
# Precio : {precio}
# Envio Gratuito: {envioGratuito}
# ''')

# -------------------------------------------------------------------
# MIN = 0
# MAX = 5
#
# num = int(input('Ingrese un numero: '))
#
# dentro_de_rango = MIN <= num <= MAX
#
# if dentro_de_rango:
#     print(f'{num} esta en el rango de 0 - 5')
# else:
#     print(f'{num} no esta en el rango  de 0 - 5')
# -------------------------------------------------------------------

# CLASE 6
# cond = True
# rta = ('Condicion Verdadera') if cond else ('Condicion Falsa')
# print(rta)
# -------------------------------------------------------------------
# num = int(input('Ingrese un numero: '))
# numText = ''
# if num == 1:
#     numText = 'Numero Uno'
# elif num == 2:
#     numText = 'Numero Dos'
# elif num == 3:
#     numText = 'Numero tres'
# else:
#     numText = 'Has ingresado un numero fura de rango'
# print(f'El numero ingresado es: {num} - {numText}')
# -------------------------------------------------------------------
# condicion = 'hola'
# if condicion == True:
#     print('Condicion Verdadera')
# elif condicion == False:
#     print('Condicón falsa')
# else:
#     print('Condicion sin especificar')
# -------------------------------------------------------------------
# a = float(input('Ingrese el valor de a: '))
# b = float(input('Ingrese el valor de b: '))
# c = float(input('Ingrese el valor de c: '))
# resultado = (a ** 3 * (b ** 2 - 2 * a * c)) / (2 * b)
# print(f'El resultado es: {resultado}')
# -------------------------------------------------------------------
# CLASE 7

# mes = 0
# while mes < 1 or mes > 12:
#     mes = int(input("Ingrese un mes: [1-12]: "))
# if mes == 1 or mes == 2 or mes == 3:
#     print("Verano")
# elif mes == 4 or mes == 5 or mes == 6:
#     print("Otoño")
# elif mes == 7 or mes == 8 or mes == 9:
#     print("Invierno")
# else:
#     print("Primavera")

# -------------------------------------------------------------------
# edad = None
# while edad is None or edad < 0:
#     edad = int(input("Ingrese su edad: "))
# if 0 < edad <=10:
#     print("La infancia es increbíle y bella")
# elif 10 < edad <= 19:
#     print()
# -------------------------------------------------------------------
# Ingresamos la nota
# nota = int(input('Ingrese la nota del alumno: '))
# if 9 <= nota <= 10:
#     print('A')
# elif 8 <= nota < 9:
#     print('B')
# elif 7 <= nota < 8:
#     print('C')
# elif 6 <= nota < 7:
#     print('D')
# elif 0 <= nota < 6:
#     print('F')
# else:
#     print('Valor incorrecto.')
# -------------------------------------------------------------------
# CLASE 8
# -------------------------------------------------------------------
# cadena = 'hola'
# for letra in cadena:
#     print(letra)
# else:
#     print('Fin del ciclo')
# -------------------------------------------------------------------
# max = 5
# contador = 0
# while contador <= max:
#     print(contador)
#     contador += 1
# min = 1
# contador = 5
# while contador >= min:
#     print(contador)
#     contador -= 1
# -------------------------------------------------------------------
# for i in range(9):
#     if i % 2 != 0:
#         continue
#     print(f'Valor : {i}')
# -------------------------------------------------------------------
# contador = 0
# while contador < 78:
#     print('Dentro del ciclo while: ', contador)
#     contador += 1
# else:
#     print('Fin del ciclo')
# -------------------------------------------------------------------
# for letra in 'Argentina':
#     if letra == 'a':
#         print(f'Letra encontrada: {letra}')
#         break
# else:
#     print(f'Fin del ciclo ')
# -------------------------------------------------------------------
# CLASE 9
# -------------------------------------------------------------------
# print('Comprobamos que el año sea bisiesto')
#
# year = int(input('Ingrese el año: '))
#
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print(f'El año {year} es bisiesto')
# else:
#     print(f'El año {year} no es bisiesto')
# -------------------------------------------------------------------
# numeros = int(input('Ingrese la cantidad de numeros a sumar: '))
# suma = 0
# for i in range(1, numeros+1):
#     suma += i
# print(f'La suma es {suma}')
# -------------------------------------------------------------------
# positivos , negativos, neutros = 0
# for i in range(10):
#     n = int(('Ingrese un numero: '))
#     if n == 0:
#         neutros += 1
#     elif n < 0:
#         negativos += 1
#     else:
#         positivos += 1
# print(f'Hay {positivos} numeros positivos')
# print(f'Hay {negativos} numeros negativos')
# print(f'Hay {neutros} numeros neutros')
# -------------------------------------------------------------------
suma = 0
calificacion_mas_baja = 99999999
catidad_alumnos = 10
for i in range(catidad_alumnos):
    nota = int(input('Ingrese una nota: '))
    suma += nota
    if nota < calificacion_mas_baja:
        calificacion_mas_baja = nota
prom = suma / catidad_alumnos
print(f'Calificacion promedio : {prom}')
print(f'Calificacion mas baja : {calificacion_mas_baja}')