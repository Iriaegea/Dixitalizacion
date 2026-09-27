#Números primos en un rango
#Pide al usuario dos enteros a y b e imprime todos los números primos entre a y b.


numero1 = int(input("Escribe un número: "))
numero2 = int(input("Escribe otro número: "))
inicio = 2
for numero in range(numero1, numero2+1):
    if ( numero % inicio != 0):
        print(f"{numero} es primo")

    inicio += 1