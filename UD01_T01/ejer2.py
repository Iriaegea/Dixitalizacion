# Números pares e impares
# Solicita al usuario una lista de números separados por espacios y muestra dos listas: una con los pares y otra con los impares.

numeros = input("Escribe numeros separados por espacios").split()   # no hace falta castearlo a string pq el input ya da string

for numero in numeros:
    n = int(numero)
    if (n % 2 == 0):
        pares = str(n) + " " 
    else:
        impares = str(n) + " "

        
print(f"Pares: {pares}")
print(f"Impares: {impares}")