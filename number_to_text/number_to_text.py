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
        if number == 0:
            return "zero"

        return "um"

