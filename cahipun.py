#Librerias
#Esta libreria permite escoger una opcion aleatoria dentro de las determinadas anteriormente.
import random

#Determinamos las opciones a escoger por la computadora
opciones = ["piedra", "papel", "tijera"]

#Le solicitamos al usuario ingresar una de las tres opciones solicitadas para llevar a cabo el juego
opcion_usuario = input("Elige piedra, papel o tijera: ").lower()

#Definimos la opcion aleatoria que escogera el computador.
opcion_computador = random.choice(opciones)

#Condicional para mostrar lo que pasaria si el usuario ingresa una opcion no valida.
if opcion_usuario not in opciones:
        #Muestra el mensaje con el resultado
        print(f"Argumento inválido: Debe ser piedra, papel o tijera.")

#Condicional para mostrar lo que pasaria si el usuario y la compotutadora escogen la misma opcion.
elif opcion_usuario == opcion_computador:
        resultado = "Empate"
        #Muestra el mensaje con el resultado
        print(f"Tú jugaste {opcion_usuario.capitalize()}\nComputador jugó {opcion_computador.capitalize()}\n{resultado}!")

#Condicional para mostrar lo que pasaria si el usuario y la compotutadora escogen distintas opciones ademas de cual opcion es la ganadora.
elif (opcion_usuario == "piedra" and opcion_computador == "tijera") or \
         (opcion_usuario == "tijera" and opcion_computador == "papel") or \
         (opcion_usuario == "papel" and opcion_computador == "piedra"):
        resultado = "Ganaste"
        #Muestra el mensaje con el resultado
        print(f"Tú jugaste {opcion_usuario.capitalize()}\nComputador jugó {opcion_computador.capitalize()}\n{resultado}!")

#Condicional para mostrar lo que pasaria si la opcion que escoge la computadora le gana al usuario.
else:
    resultado = "Perdiste"
    #Muestra el mensaje con el resultado
    print(f"Tú jugaste {opcion_usuario.capitalize()}\nComputador jugó {opcion_computador.capitalize()}\n{resultado}!")
    
