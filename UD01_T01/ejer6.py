#Números primos en un rango
#Pide al usuario dos enteros a y b e imprime todos los números primos entre a y b.


numero1 = int(input("Escribe un número: "))
numero2 = int(input("Escribe otro número: "))
inicio = 2
esPrimo = True


for numero in range(numero1, numero2+1):
    esPrimo=True
    for numero2 in range(inicio, int(numero ** 0.5)+1):
        
        if ( numero % numero2 == 0 ):
            esPrimo = False

    if(esPrimo):
        print(f"El numero {numero} es primo")