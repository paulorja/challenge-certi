DEZ1 = "dez"
DEZ2 = "vinte"
DEZ3 = "trinta"
DEZ4 = "quarenta"
DEZ5 = "cinquenta"
DEZ6 = "sessenta"
DEZ7 = "setenta"
DEZ8 = "oitenta"
DEZ9 = "noventa"

def to_text(dezena):
    return globals()["DEZ{}".format(dezena)]
