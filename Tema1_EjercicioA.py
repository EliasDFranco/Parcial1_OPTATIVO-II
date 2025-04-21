print("*** CALCULADOR DE JORNALES DIARIOS DE TRABAJADORES ***")

pagoDiurno = 10000 
pagoNocturno = 15000

areasHoras = {
    1: 6,
    2: 8,
    3: 4,
    4: 12
}

def calcuJornalDiario(turno, area):
    if turno == 1:
        pagoHora = pagoDiurno
    elif turno == 2:
        pagoHora = pagoNocturno
    else: 
        print("Este turno no existe.")
        return 0

    if area in areasHoras:
        horas = areasHoras[area]
    else:
        print("Esta área no existe.")
        return 0

    jornal = pagoHora * horas
    return jornal

turno = int(input("Ingrese el turno que desea consultar [1 = DIURNO | 2 = NOCTURNO]: "))
area = int(input("Ingrese el área que desea elegir [1 = ADMINISTRACIÓN , 2 = RECEPCIÓN , 3 = LIMPIEZA , 4 = MANTENIMIENTO]: "))

jornal = calcuJornalDiario(turno, area)

if jornal > 0:
    print(f"El jornal diario es: {jornal} Gs")
