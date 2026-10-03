# Frecuencia de caracteres
# Pide al usuario una cadena y cuenta cuántas veces aparece cada carácter usando un diccionario.

cadena = input("Escribe una cadena")
diccionario = {}
for letra in cadena:
    if letra not in diccionario:
        diccionario[letra] = 1
    else:
        diccionario[letra] +=1

print(diccionario)
