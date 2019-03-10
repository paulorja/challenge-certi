CEN1 = "cento"
CEN2 = "duzentos"
CEN3 = "trezentos"
CEN4 = "quatrocentos"
CEN5 = "quinhentos"
CEN6 = "seiscentos"
CEN7 = "setecentos"
CEN8 = "oitocentos"
CEN9 = "novecentos"

def to_text(centena):
    return globals()["CEN{}".format(centena)]
