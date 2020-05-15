#1 Escribe un programa que pida al usuario 2 números, mostrando como salida cuál es el número mayor y la diferencia de uno respecto al otro.
# En caso de que los números sean iguales, mostrarlo también en pantalla.

numero = int(input("primer numero: "))
numero_2 = int(input("segundo numero: "))

if numero < numero_2:

    resultado = numero_2 - numero
    print("el primer numero es menor al segundo por ", + resultado) 

if numero > numero_2:

    resultado = numero - numero_2
    print("la diferencia de el segundo numero con el primero es de ", + resultado)

#2 Pide al usuario que indique 2 números: uno que servirá como límite y otro para comparar. Si el segundo número es menor al primero, mostrarás
# un mensaje diciendo “El número ‘x’ se encuentra en el rango, gracias” y en caso contrario dirá “El número ‘x’ excede el límite permitido”.

limite = int(input("coloca el numero limite: "))
numero = int(input("coloca numero a comprobar: "))

if limite < numero:
    print("El número ‘{}’ excede el límite permitido".format(numero))

if limite > numero:
    print("El número ‘{}’ se encuentra en el rango, gracias".format(numero))

#3 Nuevamente pide a tu usuario que indique 3 números: un límite superior, un límite inferior y uno de comparación. Si el número de comparación 
# se encuentra entre los 2 primeros, comunicarlo en pantalla. En caso estar por debajo del límite inferior o por arriba del límite superior, 
# también mostrarlo en pantalla.

limite_superior = int(input("coloca el limite mayor: "))
limite_menor = int(input("coloca el limite menor: "))

while True:
    numero = int(input("coloca el numero a conprobar: "))

    if limite_superior < numero:
        print("te excediste del límite..")

    elif limite_menor > numero:
        print("demasiado bajo..")

    elif limite_menor < numero and limite_superior > numero:
        print("estas en entre el limite y lo minimo :)")

#4 Escribe un programa que pida al usuario ingrese su animal favorito, si coloca ‘Tortuga’, ‘tortuga’, ‘TORTUGA’ o cualquier otra variante de la
# palabra entonces mostrar en pantalla “También me gustan las tortugas”. En caso contrario mostrar el mensaje “Ese animal es genial, pero prefiero 
# las tortugas”.

animal = input("cual es tu animal favorito.?: ")

if animal.lower() == "tortuga":
    print("También me gustan las tortugas")
else:
    print("Ese animal es genial, pero prefiero las tortugas")

#5 Crea un programa que pregunte al usuario si está lloviendo, en caso de responder “sí” pregunta si está haciendo mucho viento y si responde 
# “sí” nuevamente muestra un mensaje indicando que hace mucho viento para salir con una sombrilla. En caso contrario, anima al usuario a que 
# lleve una sombrilla. Para el caso de responder “no” en la primer pregunta, entonces solo desea un bonito día.
# Considera que las respuestas pueden pasarse a minúsculas para evitar posibles errores.

while True:

    lloviendo = input("esta lloviendo.?\n")

    if lloviendo.lower() == "si":
        viento = input("esta haciendo mucho viento.?\n")

        if viento.lower() =="si":
            print("hace mucho viento como para salir con una sombrilla")

        else:
            print("te recomiendo llevar una sombrilla")
            
    elif lloviendo.lower() != "si":
        print("pues te deseo un bonito dia chabal")

#6 Pide al usuario que ingrese su edad y mostrarás un mensaje correspondiente si esta coincide con las siguientes condiciones:
# Más de 30 años: Nunca es tarde para aprender ¿Qué curso tomaremos?
# Entre 29 y 18 años: Es un momento excelente para impulsar tu carrera.
# Menos de 18 años: ¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.

while True:

    edad= int(input("dame tu edad\n"))

    if edad > 30:
        print("Nunca es tarde para aprender ¿Qué curso tomaremos?")
    if edad < 29 and edad > 18:
        print("Es un momento excelente para impulsar tu carrera.")
    if edad < 18:
        print("¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.")

#7 Crearás un script para el que el usuario indicará un número entre 1 y 6. Como respuesta se le brindará un mensaje según el número leido:
# 1 - “Hoy aprenderemos sobre prorgamación”
# 2 - “¿Qué tal tomar un curso de marketing digital?
# 3 - “Hoy es un gran día para comenzar a aprender de diseño”
# 4 - ¿Y si aprendemos algo de negocios online?
# 5 - “Veamos un par de clases sobre producción audiovisual”
# 6 - “Tal vez sea bueno desarrollar una habilidad blanda en Platzi”
# En caso indicar un número distinto, pedir al usuario que ingrese uno en el rango válido.

numero = int(input("dependiendo del nuemero que elijas te daré una respuesta\nR: "))

while True:

    if numero == 1:
        print("Hoy aprenderemos sobre prorgamación")

    elif numero == 2: 
        print("¿Qué tal tomar un curso de marketing digital?")

    elif numero == 3:
        print("Hoy es un gran día para comenzar a aprender de diseño")

    elif numero == 4:
        print("¿Y si aprendemos algo de negocios online?")

    elif numero == 5:
        print("Veamos un par de clases sobre producción audiovisual")

    elif numero == 6:
        print("Tal vez sea bueno desarrollar una habilidad blanda en Platzi")

    else: 
        print("necesitas indicar un numero valido del 1 al 6")

    numero = int(input("R:"))