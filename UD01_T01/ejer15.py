from functools import reduce



def calcularProducto(listaNumeros):
    return reduce((lambda contador, num : num * contador), listaNumeros) 
    # si no l doy valor a contador como en la línea de arriba, el valo es el primer elemento del array y pasa al siguiente
    # si quiero darle valor se hace asi: reduce((lambda contador, num : num * contador), listaNumeros, 1) se pone el valor al final


if __name__ == "__main__":
    listaNumeros = list(map(int, input("Escribe números separados por espacios: ").split()))

    print(f"El producto es : {calcularProducto(listaNumeros)}")