from functools import reduce



def MayorMenor(listaNumeros):

    listaNumeros.sort()
    mayor = listaNumeros[-1] # para pillar el del final -1 directamente
    menor = listaNumeros[0]
    media = reduce((lambda contador, num :  contador + num), listaNumeros)/len(listaNumeros) # si uso reduce hay que importarlo
    return  mayor, menor, media

    #OTRAS OPCIONES:
    # sum(listaNumeros)  ya me hace la suma sin necesidad de usr reduce
    # para sacar el mayor y menor hay funciones para listas : max(array) min(array)


if __name__ == "__main__":
    mayor = 0
    menor =0
    media = 0


    listaNumeros = list(map(float, input("Escribe las notas separadas por espacios: ").split(" ")))
    mayor, menor, media = MayorMenor(listaNumeros)


    print(f"""El número mayor es:  {mayor}
    El número menor es: {menor}
    La media es: {media}""")