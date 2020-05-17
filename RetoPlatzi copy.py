import time
import math

#1 -------------------------------------

nombre = input("tu nombre: ")

print("hola " + nombre)

#2 --------------------------------------
# Ahora que sabemos incluir nombres, podemos agregar más datos. Intentemos con un apellido para tener algo así:
# Hola, [nombre] [apellido]```

nombre = input("tu nombre: ")
apellido = input("tu apellido: ")

print("hola {} {}".format(nombre, apellido))

#3 --------------------------------------
# seguro has visto que en Platzi hay más de 600 cursos ¿puedes mostrar a que categorías corresponden en una sola línea de código?

valor = 1
print("platzi cuenta con cursos de:")
while valor <= 6:
    print("[categoria{}]".format(valor))
    valor += 15

#4 --------------------------------------
# otro clásico conocido, donde pedirás al usuario que ingrese 2 números y muestre en pantalla el resultado. Si quieres añadir 
# más dificultad puedes utilizar números con punto decimal y especificar el número de decimales después del punto.
# Ejemplo: 2.5633 + 5.6883 = 8.25

number_1 = float(input("dame el primer numero: "))
number_2 = float(input("dame el segundo numero: "))
    
result = number_1 + number_2
print(result)

#5 ----------------------------------------
#  añadiendo un extra al reto anterior ahora el usuario ingresará 3 números, sumarás los 2 primeros y el resultado será multiplicado por 
# el tercero. Añade las consideraciones del punto decimal del reto anterior.

number_1 = float(input("dame el primer numero: "))
number_2 = float(input("dame el segundo numero: "))
number_3 = float(input("por cuanto a multiplicar: "))

suma = number_1 + number_2
multiplicacion = suma * number_3
    
print("la suma de los valores da {}, y multiplicandolo por {}, da un resultado de {}".format(suma, number_3, multiplicacion))

#6 ------------------------------------------
# llegaste a una fiesta con X cantidad de rebanadas de pizza (indicadas por el usuario), después de un rato se consumió Y cantidad de rebanadas y 
# quedan Z. Fácil ¿cierto?
# El reto está en que expreses lo que sucede es una forma comprensible para cualquier persona, imprescindible pensar en tus usuarios 

print("son las 10 pm y en plena fiesta suena la puerta..")
time.sleep(2)
print("abres la puerta y resulta que es el pana carlos y lo saludas")
time.sleep(2)
pizza = int(input("despues resulta que el pana carlos trajo pizzas a lo que le preguntas cuantas pizzas trajo\nPizzas: "))
print("todos al ver su llegada y mas en concreto las {} pizzas porque hay hambre se alegran\na todos les agrada el pana carlos.".format(pizza))
time.sleep(2.5)
pizza = math.ceil(pizza / 2)
print("pero no pasan ni 5 minutos y ya en la fiesta se comieron {} cajas de pizzas.!".format(pizza))
time.sleep(2)
print("a lo que el pana carlos guarda unas cuantas para que junto a ti puedan comerselas en la mañana sin tener que preparar algo")
time.sleep(2)
print("el pana carlos es chevere... sé como carlos 😉")

#7 ------------------------------------------------------
# pide al usuario que indique su nombre y su edad. Como mensaje de salida le indicarás que edad tuvo el año pasado y cuantos años tendrá 
# el siguiente año.
# Ejemplo: [nombre] el año pasado tenías X años y el próximo año cumplirás Y años.

name = input("dame tu nombre: ")
years = int(input("dame tu edad: "))
pass_years = years - 1
future_years = years + 1
print("si hoy tienes {} significa que tuviste {} años antes.. pero en un futuro tendras {} años".format(years, pass_years, future_years))

#8 -------------------------------------------------------
# vas con tus amigos a tu restaurante favorito y acuerdan dividir la cuenta. Para facilitar las cosa pedirás al usuario que indique el total a 
# pagar, entre cuantas personas se dvidirá la cuenta, porcentaje de propina a incluir, un porcentaje de impuestos, total a pagar incluyendo
# propina más impuestos y el total a pagar por cada persona.

total = int(input("cuanto es el total a pagar: "))
personas = int(input("entre cuantos se dividira la cuenta: "))
propina = total * 0.1
impuestos = total * 0.1
cuenta_total = total + propina + impuestos
division = cuenta_total / personas
print("la cuenta en total es de {}, y como somos {} cada uno tendra que pagar un total de {}".format(cuenta_total,personas,division))

#9 ---------------------------------------------------------
#  escribe un programa al que le indiques una cantidad de días y como resultado deberá mostrar cuantas horas, minutos y segundos hay 
#  en dicha cantidad de días.

dias = int(input("dias: "))
horas = 24
minutos = 1440
segundos = 86400

if dias > 0:
    horas *= dias
    minutos *= dias
    segundos *= dias

    print("en {} dias hay un total de {} horas, {} minutos y {} segundos!..".format(dias, horas, minutos, segundos))

#10 ---------------------------------------------------------
#  hay 1.609344 km en una milla (mi). Escribe un programa en el que el usuario indique una cantidad de millas
#  y muestre en pantalla el resultado convertido a kilómetros.

kilometros = 1.609344
cantidad_millas = int(input("cuantas millas quieres convertir a KM "))
resultado = cantidad_millas * kilometros

print("en {} millas hay un total de {} kilometros".format(cantidad_millas, resultado)) 

#11 ---------------------------------------------------------
# pide al usuario ingresar un número mayor a 1000 y otro menor a 100. Indica de una forma sencilla de entender al usuario 
# cuantas veces cabe el número menor a 100 en el número mayor a 1000

numero_menor = int(input("menor de 100:  "))
numero_mayor = int(input("mayor de 1000: "))

if numero_menor <= 100 and numero_mayor >= 1000:
        
    cuantas_veces = math.floor(numero_mayor / numero_menor)
    print("el numero {} cabe {} veces en el numero {}".format(numero_menor, cuantas_veces, numero_mayor))

