import random

opciones = ["piedra", "papel", "tijera"]

opcion_usuario = input("Elige piedra, papel o tijera: ").lower()

opcion_computador = random.choice(opciones)

if opcion_usuario not in opciones:
        print(f"Argumento inválido: Debe ser piedra, papel o tijera.")

elif opcion_usuario == opcion_computador:
        resultado = "Empate"
        print(f"Tú jugaste {opcion_usuario.capitalize()}\nComputador jugó {opcion_computador.capitalize()}\n{resultado}!")

elif (opcion_usuario == "piedra" and opcion_computador == "tijera") or \
         (opcion_usuario == "tijera" and opcion_computador == "papel") or \
         (opcion_usuario == "papel" and opcion_computador == "piedra"):
        resultado = "Ganaste"
        print(f"Tú jugaste {opcion_usuario.capitalize()}\nComputador jugó {opcion_computador.capitalize()}\n{resultado}!")
else:
    resultado = "Perdiste"
    print(f"Tú jugaste {opcion_usuario.capitalize()}\nComputador jugó {opcion_computador.capitalize()}\n{resultado}!")
    
