# ===== PARTE A =====
def nombre_valido(nombre):
    pass    len(nombre) >= 3 and nombre.isalpha()

def crear_codename(nombre, nivel):
    pass    nombre[0:3].upper() + "-Lv" + str(nivel)
def vida_maxima(nivel):
    pass    100 + nivel ** 2 * 5

# ===== PARTE B =====
def clasificar_arma(poder):
    if poder >= 100:
        print ("legendaria")
    elif poder >= 50:
        print ("media")
    elif poder <= 50:
        print ("debil")
    else:
        print("Error")

def es_critico(es_magia, nivel):
    if es_magia or nivel >= 10:
        devolver = True
    else:
        devolver = False
    return devolver

def dano_base(ataque, poder, defensa):
    return (ataque + poder) - defensa
if es_critico

# ===== PARTE C =====
def porcentaje_vida(actual, maxima):
    pass    # TODO: actual / maxima * 100
def estado_vida(porcentaje):
    pass    # TODO: if/elif/else -> "CRITICO"/"HERIDO"/"SANO"
def comprar_pociones(monedas, precio):
    pass    # TODO: monedas // precio  y  monedas % precio
