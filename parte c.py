def porcentaje_vida(actual, maxima):
    porc= actual/maxima *100
    return porc
def estado_vida(porc):
    if porc <= 25:
        return "CRITICO"
    elif porc<= 50:
        return "HERIDO"
    else:
        return "SANO"
def comprar_pociones(monedas, precio):
    cantidad = monedas // precio
    vuelto = monedas % precio
    return cantidad, vuelto

print(porcentaje_vida(50, 200))
print(estado_vida(30))
print(comprar_pociones(90, 60))
