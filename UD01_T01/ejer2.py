# Números pares e impares
# Solicita al usuario una lista de números separados por espacios y muestra dos listas: una con los pares y otra con los impares.

numeros = input("Escribe numeros separados por espacios").split()   # no hace falta castearlo a string pq el input ya da string
pares = [] # para hacer listas y luego uso append
impares = []
for numero in numeros:
    n = int(numero)
    if (n % 2 == 0):
        pares.append(n)
    else:
        impares.append(n)


print(f"Pares: {pares}") # esto imprime el listado en formato de lista (feo)
print(f"Impares: {impares}")


print(f"Pares: {" ".join(pares)}\nImpares: {" ".join(impares)}) # ESTO METE UN ESPACIO ENTRE LOS ELEMENTOS DE LA LISTA (CON EL JOIN)

print(f"""Pares: {" ".join(pares)}
Impares: {" ".join(impares)}""") # ESTO IMPRIME TAL CUAL EXTÁ ESCRITO EN EL PRINT (INTROS Y TODO)

