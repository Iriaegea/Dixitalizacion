# Calculadora básica
# Implementa una calculadora que acepte dos números y una operación (+, -, *, /) introducidos por consola.
numero1 = int(input("Escribe un número: "))
operación = str(input("Qué operación quieres hacer: "))
numero2 = int(input("Escribe otro número: "))
resultado = 0
if operacion == "+":
    resultado = numero1 + numero2
    print("""{numero1} + {numero2} = {resultado} """)
elif operacion == "-":