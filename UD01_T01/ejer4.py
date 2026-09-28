# Calculadora básica
# Implementa una calculadora que acepte dos números y una operación (+, -, *, /) introducidos por consola.
<<<<<<< Updated upstream
numero1 = float(input("Escribe un número: "))
operacion = input("Qué operación quieres hacer: ")
numero2 = float(input("Escribe otro número: "))
resultado = 0

match operacion:
    case "+":
        print(f"Sumando... {numero1 + numero2}")
    case "-":
        print(f"Restanfo... {numero1-numero2}")
    case "*":
        print(f"Multiplicando... {numero1*numero2}")
    case "/":
        print(f"Dividiendo... {numero1/numero2}")
    case "_": 
        print(f"Error... ")