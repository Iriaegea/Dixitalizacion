#Diccionario inverso
#Dado un diccionario con pares clave-valor, crea otro con los valores como claves y las claves como valores.

diccionario1 ={"nombre":"Iria", "edad": 21 }
diccionario2 = {}
for clave, valor in diccionario1.items() :
    diccionario2[valor] = clave


print(f"Resultado: {diccionario2}")