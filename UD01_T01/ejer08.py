#Juego de adivinanza
#El programa genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo recibiendo pistas de "mayor" o "menor".
import random

intentos = 10
numeroSecreto = random.randint(1,100)
print(f"Tienes 10 intentos")

numero = int(input("Adivina el número que estoy pensando: "))

while numero != numeroSecreto & intentos > 0:
    
    if numero > numeroSecreto :
        print(f"Mi número es mas pequeño") 
    elif numero < numeroSecreto:
        print(f"Mi número es más grande")
    

    intentos -=1
    print(f"Te quedan {intentos} intentos")

    numero = int(input("Adivina el número que estoy pensando: "))
if intentos > 0:
    print(f"HAS ACERTADI¡O!!!")
else:
    print(f"NO HAS ACERTADO!!! Mi número era el {numeroSecreto}")