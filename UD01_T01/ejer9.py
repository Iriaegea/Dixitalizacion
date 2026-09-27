#Diccionario de frecuencias de palabras
#Pide al usuario una frase y construye un diccionario con la frecuencia de cada palabra.

diccionario = {}

frase = input("Escribe una frase: ")
arrayFrase = frase.split()

for palabra in arrayFrase:
    
    if not palabra in diccionario :
        diccionario[palabra] = 1
    else :
        diccionario[palabra] += 1



for palabra, cantidad in diccionario.items():
    print(f"{palabra} : {cantidad}")