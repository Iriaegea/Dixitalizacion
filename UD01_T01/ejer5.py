#Ordenación de palabras
#El usuario introduce una frase. Muestra las palabras ordenadas alfabéticamente y por longitud.

frase = input("Introduce una frase: ")
arrayFrase = frase.split()
print(f"Frase ordenada alfabéticamente: ")
arrayFrase.sort()
print(" ".join(arrayFrase))
print(f"frase ordenada por longitud:")
arrayFrase.sort(key=len)
print(" ".join(arrayFrase))



# se puede usar lambda, que es una foma corta de hacer una funcion:
arrayFrase.sort(key(lambda palabra : (palabra.lower(), len(palabra)))
#en key meto la funcion que devuelve lo que hay después de los dos puntos. Primero hace lo de la izquierda y si sale que hay cosas empatadas hace la segunda
