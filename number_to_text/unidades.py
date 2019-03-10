ZERO = "zero"

UNI1 = "um"
UNI2 = "dois"
UNI3 = "tres"
UNI4 = "quatro"
UNI5 = "cinco"
UNI6 = "seis"
UNI7 = "sete"
UNI8 = "oito"
UNI9 = "nove"

def to_text(unidade):
    return globals()["UNI{}".format(unidade)]
