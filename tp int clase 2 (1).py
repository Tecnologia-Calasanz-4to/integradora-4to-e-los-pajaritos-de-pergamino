
def nombre_valido(nombre):
    if len(nombre) >= 3 and nombre.isalpha():
        devolver= True
    else:
        devolver= False
    return devolver

def crear_codename(nombre, nivel):
    a =  nombre[0:3].upper() + "-Lv" + str(nivel)
    return a

def vida_maxima(nivel):
     return 100 + (nivel ** 2) * 5

# ===== PARTE B =====
def clasificar_arma(poder):
    if arm == legendaria:
        d
    elif arm == media:
        d
    elif arm == debil:
        d
    else:
        print("Error")
    pass    # TODO: if/elif/else -> "Legendaria"/"Media"/"Debil"
def es_critico(es_magica, nivel):
    pass    # TODO: es_magica or nivel >= 10
def dano_base(ataque, poder, defensa):
    pass    # TODO: (ataque + poder) - defensa
def dano_total(ataque, poder, defensa, critico):
    pass    # TODO: si critico -> dano_base(...) * 2 ; si no -> dano_base(...)

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



# ===== PARTE D =====
def puede_atacar(energia, esta_aturdido):
    if  energia > 0 and not esta_aturdido == False:
        return True
    else:
        return False
def vida_restante(vida, dano):
    vidar= vida - dano
    return vidar
def gana(vida_heroe, vida_enemigo):
    if vida_heroe > vida_enemigo:
        return True
    else:
        return False

nombre= input("Dame tu nombre")
print ("Nombre valido", nombre_valido(nombre))
print ("Codename", crear_codename(nombre, 100))
print("Vida maxima", vida_maxima(5))
print(porcentaje_vida(50, 200))
print(estado_vida(30))
print(comprar_pociones(90, 60))
print (puede_atacar(3, False))
print(vida_restante(10, 8))
print(gana(2, 9))
