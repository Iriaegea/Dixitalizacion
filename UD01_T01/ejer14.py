
def MayorMenor(listaNumeros):

    listaNumeros.sort()
    return [(listaNumeros[len(listaNumeros)]),(listaNumeros[0]),((reduce(lambda contador, num : contador = contador + num), listaNumeros)/len(listaNumeros))]


if __name__ == "__main__":

    listaNumeros = list(map(float, input("Escribe las notas separadas por espacios: ").split(" ")))
    listaMayorMenorMedia = MayorMenor(listaNumeros)


    print(f"""El número mayor es:  {}
    El número menor es: {}
    La media es: {}""")