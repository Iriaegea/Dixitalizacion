# Conversor de temperaturas
# Escribe un programa que pida al usuario una temperatura en grados Celsius y la convierta a Fahrenheit y Kelvin.

celsius = float(input("Escribe una temperatura en Celsius para pasarla a Fahrenheit y Kelvin"))

print(f"Celsius = {celsius}, Fahrenheit = {float((celsius*1.8)+32)}, Kelvin = {float(celsius + 273.15)}")


