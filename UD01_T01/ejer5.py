#Ordenación de palabras
#El usuario introduce una frase. Muestra las palabras ordenadas alfabéticamente y por longitud.

frase = input("Introduce una frase: ")
arrayFrase = frase.split()

arrayFrase.sort()
arrayFrase.sort(key=len)

print(" ".join(arrayFrase))