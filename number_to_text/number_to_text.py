import unidades as uni
import dezenas as dez
import centenas as cen


class NumberToText():

    def is_valid_number(self, number):
        if not isinstance(number, int):
            return False
        if number > 99999 or number < -99999:
            return False
        return True

    def number_to_text(self, number):
        if not self.is_valid_number(number):
            return None

        txt_sinal = None
        txt_unidade = None
        txt_dezena = None
        txt_centena = None
        txt_unidade_milhar = None
        txt_dezena_milhar = None

        if number < 0:
            txt_sinal = "menos"

        if number == 0:
            txt_unidade = uni.ZERO

        if number != 0:
            unidade = str(number)[-1]
            if unidade != "0":
                txt_unidade = uni.to_text(unidade)

        if number > 9 or number < -9:
            dezena = str(number)[-2]
            if dezena != "0":
                txt_dezena = dez.to_text(dezena)

        if number > 99 or number < -99:
            centena = str(number)[-3]
            if centena != "0":
                txt_centena = cen.to_text(centena)

        if number > 999 or number < -999:
            unidade_milhar = str(number)[-4]
            if unidade_milhar != "0":
                txt_unidade_milhar = uni.to_text(unidade_milhar)

        if number > 9999 or number < -9999:
            dezena_milhar = str(number)[-5]
            txt_dezena_milhar = dez.to_text(dezena_milhar)

        txt_result = ""

        if txt_sinal != None:
            txt_result += "{}".format(txt_sinal)

        if txt_dezena_milhar != None:
            txt_result += " {}".format(txt_dezena_milhar)
            if txt_unidade_milhar != None:
                txt_result = "{} e".format(txt_result)

        if txt_unidade_milhar != None:
            txt_result += " {}".format(txt_unidade_milhar)

        if txt_dezena_milhar != None or txt_unidade_milhar != None:
            txt_result += " mil"

        if (txt_dezena_milhar != None or txt_unidade_milhar != None) and (txt_centena != None or txt_dezena != None or txt_unidade != None):
            txt_result = "{} e".format(txt_result)


        if txt_centena != None:
            txt_result += " {}".format(txt_centena)
            if txt_dezena != None:
                txt_result = "{} e".format(txt_result)

        if txt_dezena != None:
            txt_result += " {}".format(txt_dezena)
            if txt_unidade != None:
                txt_result = "{} e".format(txt_result)

        if txt_unidade != None:
            txt_result += " {}".format(txt_unidade)

        return txt_result.strip()
