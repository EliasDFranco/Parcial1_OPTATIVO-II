print("*** CALCULADOR DE PORCENTAJE DE ENCUESTAS ***")
import random 

personasEncuestadas = 20
generos = ["Mujer", "Hombre"]
respuestas = []

for x in range(personasEncuestadas):
    valor = random.randint(0,1) 
    if valor == 0:
        respuestas.append("Mujer")
        
    elif valor == 1:
        respuestas.append("Hombre")
        
cantMujeres = respuestas.count("Mujer")
cantHombres = respuestas.count("Hombre")

porcentajeMujeres = (cantMujeres / personasEncuestadas ) * 100
porcentajeHombres = (cantHombres / personasEncuestadas ) * 100

print(f"La cantidad de mujeres: {cantMujeres} , su porcentaje es: ({porcentajeMujeres:.2f}) % ")
print(f"La cantidad de hombres: {cantHombres} , su porcentaje es: ({porcentajeHombres:.2f}) % ")

