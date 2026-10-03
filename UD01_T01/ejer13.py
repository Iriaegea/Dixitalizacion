# Funciones simples
# Declara una función es_par(n) que devuelva True si n es par y False en caso contrario.


def es_par(n):
    return n % 2 ==0
        

if __name__ == "__main__":

    n = int(input("Escribe un número: "))
    if es_par(n):
        print(f"Es par")
    else :
        print(f"No es par")

