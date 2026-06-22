def porcentaje_vida(actual, maxima):
    porc= actual/maxima *100
    return porcentaje
def estado_vida(porcentaje):
    if porcentaje <= 25:
        return "CRITICO"
    elif porcentaje <= 50:
        return "HERIDO"
    else:
        return "SANO"
def comprar_pociones(monedas, precio):
    cantidad = monedas // precio
    vuelto = monedas % precio
    return cantidad, vuelto


