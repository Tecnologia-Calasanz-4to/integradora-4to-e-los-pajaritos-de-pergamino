# ===== PARTE B =====
def clasificar_arma(poder):
    if poder >= 100:
        return ("legendaria")
    elif poder >= 50:
        return ("media")
    elif poder <= 50:
        return ("debil")
    else:
        return("Error")

def es_critico(es_magia, nivel):
    if es_magia or nivel >= 10:
        return True
    else:
        return False
    return critico

def dano_base(ataque, poder, defensa):
    a = (ataque + poder) - defensa
    return a

def dano_total(ataque, poder, defensa, critico):
    if critico==True:
        return dano_base(ataque, poder, defensa) * 2
    else:
        return dano_base(ataque, poder, defensa)
    

resultado_arma = clasificar_arma (100)
resultado_critico = es_critico (True, 30)
resultado_base = dano_base (100, 150, 200)
dano_final = dano_total (100, 150, 200,250)

print("el poder del arma es:", resultado_arma)
print("golpe critico:", resultado_critico)
print("daño base realizado es:", resultado_base)
print("daño total es:", dano_final)
