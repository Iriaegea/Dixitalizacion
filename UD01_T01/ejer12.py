#Diccionarios de listas (agenda)
#Crea un programa que guarde contactos en un diccionario con nombre y una lista de  teléfonos. Permite añadir y buscar contactos por nombre.


agenda = {}
opcion = 1
nombre = ""
numero = ""
while opcion != 0 :
    print(f"""MENU:
    1. CREAR CONTACTO
    2. AÑADIR NUEVO NÚMERO A UN CONTACTO
    0. SALIR""")
    opcion = int(input("Elige una opción: (1/2/0)"))

    match opcion:
        case 1:
            nombre = input("Escribe el nombre: ").lower()
            numero = input("Escribe el número: ")                      
            if nombre not in agenda : 
                agenda[nombre] = [numero] #primero tengo q crear el array 
            else:
                agenda[nombre].append(numero) #se lo añade al array porque si no lo sustituyo
        case 2: 
            nombre = input("Escribe el nombre: ").lower()
            
            if nombre not in agenda : 
               print(f"El contacto no existe, hay que crearlo primero")
            else:
                numero = input("Escribe el número: ")
                agenda[nombre].append(numero)
            
        case 0:
            print(f"Has salido del programa")
        case _:
            print(f"Algo ha salido mal")

print(f"{agenda}")