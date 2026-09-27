#Gestión de notas
#Solicita al usuario nombres y calificaciones de varios alumnos (hasta que escriba "fin"). Al final muestra:

#Nota media
#Nota más alta
#Nota más baja
import sys


alumnos={}
notaMedia=0
totalNotas = 0
sumaTotal = 0
notaBaja = sys.maxsize
notaAlta = -sys.maxsize-1
notaActual = 0
nombrePeorAlumno=""
nombreMejorAlumno=""
respuesta = ""
while respuesta.lower() != "fin":
    respuesta=input("Escribe el nombre de un alumno: ")
    
    if(respuesta.lower() != "fin"):
        notaActual= int(input("Nota: "))
        totalNotas +=1
        sumaTotal += notaActual
        if(notaActual >= notaAlta):
            notaAlta = notaActual
            nombreMejorAlumno = respuesta
        elif (notaActual <= notaBaja):
            notaBaja = notaActual
            nombrePeorAlumno = respuesta
        
        


print(f"El alumno con la mejor nota: {nombreMejorAlumno} con un : {notaAlta}")
print(f"El alumno con la peor nota: {nombrePeorAlumno} con un : {notaBaja}")
print(f"La media de las notas es: {sumaTotal/totalNotas}")
