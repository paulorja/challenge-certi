E100 = "cem"

E11 = "onze"
E12 = "doze"
E13 = "treze"
E13 = "treze"
E14 = "catorze"
E15 = "quinze"
E16 = "dezesseis"
E17 = "dezessete"
E18 = "dezoito"
E19 = "dezenove"

LIST_EXCECOES_DEZENAS = ["11", "12", "13", "14", "15", "16", "17", "18", "19"]

def to_text(dezena_excecao):
    return globals()["E{}".format(dezena_excecao)]
