# Funciones simples
# Declara una función es_par(n) que devuelva True si n es par y False en caso contrario.


def es_par(n):
    
    if numero %2 ==0:
        return True
    
    return False

if __name__ == "__main__":

n = int(input("Escribe un número: "))
if es_par(numero):
    print(f"Es par")
else :
    print(f"No es par")

